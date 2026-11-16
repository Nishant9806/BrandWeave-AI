from uuid import UUID
from app.schemas.content import ContentCorrection
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Organization, User, Submission, ContentVersion
from app.services.audit_logger import record_audit_event
from app.schemas.content import ContentCreate, ContentResponse
from app.db.models import Review

router = APIRouter()


@router.post("/content", response_model=ContentResponse)
def create_content(payload: ContentCreate, db: Session = Depends(get_db)):
    organization = db.query(Organization).filter_by(
        name="TechNova"
    ).first()

    user = db.query(User).filter_by(
        email="creator@technova.demo"
    ).first()

    if not organization or not user:
        raise HTTPException(
            status_code=500,
            detail="Demo organization or creator is missing."
        )

    try:
        submission = Submission(
            organization_id=organization.id,
            created_by=user.id,
            title=payload.title,
            content_type=payload.content_type,
            current_status="DRAFT"
        )

        db.add(submission)
        db.flush()

        version = ContentVersion(
            submission_id=submission.id,
            version_number=1,
            content=payload.content,
            created_by=user.id
        )

        db.add(version)
        record_audit_event(
            db, organization.id, "CONTENT_CREATED",
            user.id, submission.id,
            {"title": submission.title, "version": 1}
        )
        db.commit()
        db.refresh(submission)
        db.refresh(version)

        return ContentResponse(
            submission_id=str(submission.id),
            version_id=str(version.id),
            version_number=version.version_number,
            title=submission.title,
            content_type=submission.content_type,
            status=submission.current_status
        )

    except Exception:
        db.rollback()
        raise


@router.post("/content/{submission_id}/corrections", response_model=ContentResponse)
def create_correction(
    submission_id: str,
    payload: ContentCorrection,
    db: Session = Depends(get_db)
):
    try:
        parsed_id = UUID(submission_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid submission ID.")

    submission = db.query(Submission).filter(
        Submission.id == parsed_id
    ).first()

    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found.")

    latest_version = (
        db.query(ContentVersion)
        .filter(ContentVersion.submission_id == submission.id)
        .order_by(ContentVersion.version_number.desc())
        .first()
    )

    if not latest_version:
        raise HTTPException(status_code=404, detail="Original content not found.")

    try:
        new_version = ContentVersion(
            submission_id=submission.id,
            version_number=latest_version.version_number + 1,
            content=payload.content,
            created_by=latest_version.created_by
        )

        submission.current_status = "RESUBMITTED"

        db.add(new_version)
        record_audit_event(
            db, submission.organization_id, "CONTENT_CORRECTED",
            new_version.created_by, submission.id,
            {"version": new_version.version_number}
        )
        db.commit()
        db.refresh(new_version)

        return ContentResponse(
            submission_id=str(submission.id),
            version_id=str(new_version.id),
            version_number=new_version.version_number,
            title=submission.title,
            content_type=submission.content_type,
            status=submission.current_status
        )

    except Exception:
        db.rollback()
        raise

@router.get("/content")
def list_submissions(db: Session = Depends(get_db)):
    submissions = (
        db.query(Submission)
        .order_by(Submission.created_at.desc())
        .all()
    )

    results = []

    for submission in submissions:
        latest_version = (
            db.query(ContentVersion)
            .filter(ContentVersion.submission_id == submission.id)
            .order_by(ContentVersion.version_number.desc())
            .first()
        )

        results.append({
            "submission_id": str(submission.id),
            "title": submission.title,
            "content_type": submission.content_type,
            "status": submission.current_status,
            "latest_version": latest_version.version_number if latest_version else None,
            "created_at": submission.created_at.isoformat()
        })

    return results