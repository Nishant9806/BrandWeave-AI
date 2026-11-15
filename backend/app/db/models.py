
import uuid

from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    Float,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    JSON,
    func,
)
from sqlalchemy.dialects.postgresql import UUID, JSONB

from app.db.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    name = Column(String(150), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(30), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class BrandGuideline(Base):
    __tablename__ = "brand_guidelines"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    title = Column(String(200), nullable=False)
    file_path = Column(Text, nullable=True)
    extracted_text = Column(Text, nullable=True)
    status = Column(String(30), nullable=False)
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class BrandFact(Base):
    __tablename__ = "brand_facts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    fact_key = Column(String(150), nullable=False)
    fact_value = Column(Text, nullable=False)
    source_guideline_id = Column(UUID(as_uuid=True), ForeignKey("brand_guidelines.id"), nullable=True)
    status = Column(String(30), nullable=False)
    verified_at = Column(DateTime(timezone=True), nullable=True)
    expires_at = Column(DateTime(timezone=True), nullable=True)


class BrandTerm(Base):
    __tablename__ = "brand_terms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    term = Column(String(200), nullable=False)
    term_type = Column(String(30), nullable=False)
    replacement = Column(String(200), nullable=True)
    explanation = Column(Text, nullable=True)


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    title = Column(String(200), nullable=False)
    content_type = Column(String(50), nullable=False)
    current_status = Column(String(40), nullable=False, default="DRAFT")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class ContentVersion(Base):
    __tablename__ = "content_versions"
    __table_args__ = (
        UniqueConstraint("submission_id", "version_number", name="uq_submission_version"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    submission_id = Column(UUID(as_uuid=True), ForeignKey("submissions.id"), nullable=False)
    version_number = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Review(Base):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    version_id = Column(UUID(as_uuid=True), ForeignKey("content_versions.id"), nullable=False)
    status = Column(String(30), nullable=False, default="PENDING")
    total_findings = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    completed_at = Column(DateTime(timezone=True), nullable=True)


class Finding(Base):
    __tablename__ = "findings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    review_id = Column(UUID(as_uuid=True), ForeignKey("reviews.id"), nullable=False)
    category = Column(String(50), nullable=False)
    severity = Column(String(20), nullable=False)
    confidence = Column(Float, nullable=False)
    original_text = Column(Text, nullable=False)
    explanation = Column(Text, nullable=False)
    suggested_fix = Column(Text, nullable=True)
    source_type = Column(String(30), nullable=True)
    source_id = Column(UUID(as_uuid=True), nullable=True)
    status = Column(String(30), nullable=False, default="OPEN")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Approval(Base):
    __tablename__ = "approvals"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    submission_id = Column(UUID(as_uuid=True), ForeignKey("submissions.id"), nullable=False)
    version_id = Column(UUID(as_uuid=True), ForeignKey("content_versions.id"), nullable=False)
    reviewer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    decision = Column(String(30), nullable=False)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class AuditEvent(Base):
    __tablename__ = "audit_events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    submission_id = Column(UUID(as_uuid=True), ForeignKey("submissions.id"), nullable=True)
    action = Column(String(100), nullable=False)
    details = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
