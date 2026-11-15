
from datetime import datetime, timezone
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import (
    Submission,
    ContentVersion,
    Review,
    Finding,
    BrandFact,
    BrandTerm
)
from app.services.brand_engine.brand_reviewer import review_brand_content
from app.schemas.content import ReviewResponse, FindingResponse

router = APIRouter()


@router.post("/content/{submission_id}/review", response_model=ReviewResponse)
def review_submission(
    submission_id: str,
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

    version = (
        db.query(ContentVersion)
        .filter(ContentVersion.submission_id == submission.id)
        .order_by(ContentVersion.version_number.desc())
        .first()
    )

    if not version:
        raise HTTPException(status_code=404, detail="Content version not found.")

    result = review_brand_content(version.content)

    if result["status"] != "COMPLETED":
        raise HTTPException(status_code=400, detail=result.get("message", "Review failed."))

    try:
        review = Review(
            version_id=version.id,
            status="COMPLETED",
            total_findings=result["total_findings"],
            completed_at=datetime.now(timezone.utc)
        )

        db.add(review)
        db.flush()

        saved_findings = []

        for item in result["findings"]:
            source_id = None

            if item.get("source_type") == "BRAND_FACT" and item.get("source_id"):
                source = db.query(BrandFact).filter_by(
                    organization_id=submission.organization_id,
                    fact_key=item["source_id"]
                ).first()

                if source:
                    source_id = source.id

            elif item.get("source_type") == "BRAND_TERM" and item.get("source_id"):
                source = db.query(BrandTerm).filter_by(
                    organization_id=submission.organization_id,
                    term=item["source_id"]
                ).first()

                if source:
                    source_id = source.id

            finding = Finding(
                review_id=review.id,
                category=item["category"],
                severity=item["severity"],
                confidence=item["confidence"],
                original_text=item["original_text"],
                explanation=item["explanation"],
                suggested_fix=item.get("suggested_fix"),
                source_type=item.get("source_type"),
                source_id=source_id,
                status=item.get("status", "OPEN")
            )

            db.add(finding)
            saved_findings.append(finding)

        db.commit()

        return ReviewResponse(
            review_id=str(review.id),
            status=review.status,
            total_findings=review.total_findings,
            findings=[
                FindingResponse(
                    id=str(f.id),
                    category=f.category,
                    severity=f.severity,
                    confidence=f.confidence,
                    original_text=f.original_text,
                    explanation=f.explanation,
                    suggested_fix=f.suggested_fix,
                    status=f.status
                )
                for f in saved_findings
            ]
        )

    except Exception:
        db.rollback()
        raise


@router.get(
    "/content/{submission_id}/findings",
    response_model=ReviewResponse
)
def get_submission_findings(
    submission_id: str,
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

    review = (
        db.query(Review)
        .join(
            ContentVersion,
            Review.version_id == ContentVersion.id
        )
        .filter(ContentVersion.submission_id == parsed_id)
        .order_by(Review.created_at.desc())
        .first()
    )

    if not review:
        raise HTTPException(
            status_code=404,
            detail="No review found for this submission."
        )

    findings = (
        db.query(Finding)
        .filter(Finding.review_id == review.id)
        .order_by(Finding.created_at.asc())
        .all()
    )

    return ReviewResponse(
        review_id=str(review.id),
        status=review.status,
        total_findings=review.total_findings,
        findings=[
            FindingResponse(
                id=str(f.id),
                category=f.category,
                severity=f.severity,
                confidence=f.confidence,
                original_text=f.original_text,
                explanation=f.explanation,
                suggested_fix=f.suggested_fix,
                status=f.status
            )
            for f in findings
        ]
    )
