from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Organization, AuditEvent

router = APIRouter()


@router.get("/audit")
def get_audit_events(db: Session = Depends(get_db)):
    organization = (
        db.query(Organization)
        .filter(Organization.name == "TechNova")
        .first()
    )

    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found.")

    events = (
        db.query(AuditEvent)
        .filter(AuditEvent.organization_id == organization.id)
        .order_by(AuditEvent.created_at.desc())
        .all()
    )

    return [
        {
            "id": str(event.id),
            "action": event.action,
            "user_id": str(event.user_id) if event.user_id else None,
            "submission_id": str(event.submission_id) if event.submission_id else None,
            "details": event.details,
            "created_at": event.created_at.isoformat(),
        }
        for event in events
    ]
