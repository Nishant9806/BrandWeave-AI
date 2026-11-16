from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import (
    Organization,
    Submission,
    ContentVersion,
    User,
    Review,
)

router = APIRouter()


@router.get("/content/{submission_id}/history")
def get_submission_history(
    submission_id: str,
    db: Session = Depends(get_db),
):
    try:
        parsed_id = UUID(submission_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid submission ID.")

    organization = (
        db.query(Organization)
        .filter(Organization.name == "TechNova")
        .first()
    )

    if not organization:
        raise HTTPException(status_code=404, detail="Brand organization not found.")

    submission = (
        db.query(Submission)
        .filter(
            Submission.id == parsed_id,
            Submission.organization_id == organization.id,
        )
        .first()
    )

    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found.")

    versions = (
        db.query(ContentVersion)
        .filter(ContentVersion.submission_id == submission.id)
        .order_by(ContentVersion.version_number.asc())
        .all()
    )

    history = []

    for version in versions:
        creator = db.query(User).filter(User.id == version.created_by).first()

        review = (
            db.query(Review)
            .filter(Review.version_id == version.id)
            .order_by(Review.created_at.desc())
            .first()
        )

        history.append({
            "version_id": str(version.id),
            "version_number": version.version_number,
            "content": version.content,
            "created_by": {
                "id": str(creator.id),
                "name": creator.name,
                "email": creator.email,
            } if creator else None,
            "created_at": version.created_at.isoformat(),
            "review": {
                "review_id": str(review.id),
                "status": review.status,
                "total_findings": review.total_findings,
                "created_at": review.created_at.isoformat(),
                "completed_at": review.completed_at.isoformat() if review.completed_at else None,
            } if review else None,
        })

    return {
        "submission_id": str(submission.id),
        "title": submission.title,
        "content_type": submission.content_type,
        "current_status": submission.current_status,
        "total_versions": len(history),
        "versions": history,
    }
