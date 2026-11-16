from app.db.models import AuditEvent


def record_audit_event(
    db,
    organization_id,
    action,
    user_id=None,
    submission_id=None,
    details=None,
):
    event = AuditEvent(
        organization_id=organization_id,
        user_id=user_id,
        submission_id=submission_id,
        action=action,
        details=details or {},
    )
    db.add(event)
