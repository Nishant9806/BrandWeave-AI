
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.audit_logger import record_audit_event
from app.db.models import (
    Submission,
    ContentVersion,
    User,
    Approval,
    Review,
    Finding
)

router = APIRouter()


class ApprovalRequest(BaseModel):
    decision: str = Field(
        ...,
        pattern="^(APPROVED|REJECTED|CHANGES_REQUESTED)$"
    )
    comment: str | None = None


@router.post("/content/{submission_id}/approval")
def decide_submission(
    submission_id: str,
    payload: ApprovalRequest,
    db: Session = Depends(get_db)
):
    try:
        parsed_id = UUID(submission_id)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid submission ID."
        )

    submission = db.query(Submission).filter(
        Submission.id == parsed_id
    ).first()

    if not submission:
        raise HTTPException(
            status_code=404,
            detail="Submission not found."
        )

    manager = db.query(User).filter_by(
        organization_id=submission.organization_id,
        role="MANAGER"
    ).first()

    if not manager:
        raise HTTPException(
            status_code=404,
            detail="Demo manager not found."
        )

    latest_version = (
        db.query(ContentVersion)
        .filter(ContentVersion.submission_id == submission.id)
        .order_by(ContentVersion.version_number.desc())
        .first()
    )

    if not latest_version:
        raise HTTPException(
            status_code=404,
            detail="Content version not found."
        )

    # Approval requires a completed review of the latest version.
    if payload.decision == "APPROVED":

        latest_review = (
            db.query(Review)
            .filter(Review.version_id == latest_version.id)
            .order_by(Review.created_at.desc())
            .first()
        )

        if not latest_review or latest_review.status != "COMPLETED":
            raise HTTPException(
                status_code=400,
                detail="A completed review is required before approval."
            )

        # Only resolved or rejected findings are considered closed.
        unresolved_findings = db.query(Finding).filter(
            Finding.review_id == latest_review.id,
            Finding.status.notin_(["RESOLVED", "REJECTED"])
        ).count()

        if unresolved_findings > 0:
            raise HTTPException(
                status_code=400,
                detail=f"Approval blocked. {unresolved_findings} unresolved finding(s) remain."
            )

    try:
        approval = Approval(
            submission_id=submission.id,
            version_id=latest_version.id,
            reviewer_id=manager.id,
            decision=payload.decision,
            comment=payload.comment
        )

        submission.current_status = payload.decision

        db.add(approval)
        record_audit_event(
            db, submission.organization_id, "APPROVAL_DECIDED",
            manager.id, submission.id,
            {"decision": approval.decision, "comment": approval.comment}
        )
        db.commit()
        db.refresh(approval)

        return {
            "approval_id": str(approval.id),
            "submission_id": str(submission.id),
            "version_id": str(latest_version.id),
            "version_number": latest_version.version_number,
            "decision": approval.decision,
            "comment": approval.comment,
            "reviewer": manager.name,
            "status": submission.current_status
        }

    except Exception:
        db.rollback()
        raise
