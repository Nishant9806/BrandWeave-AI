from collections import Counter

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import (
    Organization,
    Submission,
    ContentVersion,
    Review,
    Finding,
    Approval,
)

router = APIRouter()


@router.get("/analytics")
def get_analytics(db: Session = Depends(get_db)):
    organization = (
        db.query(Organization)
        .filter(Organization.name == "TechNova")
        .first()
    )

    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found.")

    submissions = (
        db.query(Submission)
        .filter(Submission.organization_id == organization.id)
        .all()
    )

    submission_ids = [item.id for item in submissions]

    versions_query = (
        db.query(ContentVersion)
        .join(Submission, ContentVersion.submission_id == Submission.id)
        .filter(Submission.organization_id == organization.id)
    )

    reviews_query = (
        db.query(Review)
        .join(ContentVersion, Review.version_id == ContentVersion.id)
        .join(Submission, ContentVersion.submission_id == Submission.id)
        .filter(Submission.organization_id == organization.id)
    )

    findings_query = (
        db.query(Finding)
        .join(Review, Finding.review_id == Review.id)
        .join(ContentVersion, Review.version_id == ContentVersion.id)
        .join(Submission, ContentVersion.submission_id == Submission.id)
        .filter(Submission.organization_id == organization.id)
    )

    approvals_query = (
        db.query(Approval)
        .join(Submission, Approval.submission_id == Submission.id)
        .filter(Submission.organization_id == organization.id)
    )

    submission_status = Counter(item.current_status for item in submissions)
    review_status = Counter(item.status for item in reviews_query.all())
    finding_status = Counter(item.status for item in findings_query.all())
    approval_decisions = Counter(item.decision for item in approvals_query.all())

    return {
        "organization": organization.name,
        "submissions": {
            "total": len(submissions),
            "by_status": dict(submission_status),
        },
        "content_versions": {
            "total": versions_query.count(),
        },
        "reviews": {
            "total": reviews_query.count(),
            "by_status": dict(review_status),
        },
        "findings": {
            "total": findings_query.count(),
            "unresolved": sum(
                count for status, count in finding_status.items()
                if status.upper() not in ("RESOLVED", "CLOSED")
            ),
            "by_status": dict(finding_status),
        },
        "approvals": {
            "total": approvals_query.count(),
            "by_decision": dict(approval_decisions),
        },
    }
