# BrandWeave AI — Database Schema

## 1. Database Technology

- Database: PostgreSQL
- ORM: SQLAlchemy
- Migration Tool: Alembic
- Primary Key: UUID
- Timestamp Standard: UTC

## 2. Database Tables

### 2.1 organizations

Stores organisation information.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| name | VARCHAR(150) | NOT NULL |
| description | TEXT | NULL |
| created_at | TIMESTAMP | NOT NULL |

### 2.2 users

Stores user information and roles.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| organization_id | UUID | Foreign Key |
| name | VARCHAR(150) | NOT NULL |
| email | VARCHAR(255) | UNIQUE, NOT NULL |
| password_hash | VARCHAR(255) | NOT NULL |
| role | VARCHAR(30) | NOT NULL |
| created_at | TIMESTAMP | NOT NULL |

Roles: ADMIN, CREATOR, MANAGER.

### 2.3 brand_guidelines

Stores uploaded brand documents.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| organization_id | UUID | Foreign Key |
| title | VARCHAR(200) | NOT NULL |
| file_path | TEXT | NULL |
| extracted_text | TEXT | NULL |
| status | VARCHAR(30) | NOT NULL |
| uploaded_at | TIMESTAMP | NOT NULL |

### 2.4 brand_facts

Stores approved brand and product information.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| organization_id | UUID | Foreign Key |
| fact_key | VARCHAR(150) | NOT NULL |
| fact_value | TEXT | NOT NULL |
| source_guideline_id | UUID | Foreign Key, NULL |
| status | VARCHAR(30) | NOT NULL |
| verified_at | TIMESTAMP | NULL |
| expires_at | TIMESTAMP | NULL |

Example:
- product_name: SmartWatch Pro
- battery_life: 24 hours
- price: ₹1,499

### 2.5 brand_terms

Stores preferred and prohibited terminology.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| organization_id | UUID | Foreign Key |
| term | VARCHAR(200) | NOT NULL |
| term_type | VARCHAR(30) | NOT NULL |
| replacement | VARCHAR(200) | NULL |
| explanation | TEXT | NULL |

Term types: PREFERRED, PROHIBITED.

### 2.6 submissions

Stores content submitted for brand review.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| organization_id | UUID | Foreign Key |
| created_by | UUID | Foreign Key |
| title | VARCHAR(200) | NOT NULL |
| content_type | VARCHAR(50) | NOT NULL |
| current_status | VARCHAR(40) | NOT NULL |
| created_at | TIMESTAMP | NOT NULL |
| updated_at | TIMESTAMP | NOT NULL |

Statuses:
DRAFT, IN_REVIEW, CHANGES_REQUESTED, RESUBMITTED, APPROVED, REJECTED.

### 2.7 content_versions

Maintains every version of submitted content.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| submission_id | UUID | Foreign Key |
| version_number | INTEGER | NOT NULL |
| content | TEXT | NOT NULL |
| created_by | UUID | Foreign Key |
| created_at | TIMESTAMP | NOT NULL |

Each submission can have multiple versions.

The original content must never be overwritten.

### 2.8 findings

Stores issues detected by the review engine.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| version_id | UUID | Foreign Key |
| category | VARCHAR(50) | NOT NULL |
| severity | VARCHAR(20) | NOT NULL |
| confidence | FLOAT | NOT NULL |
| original_text | TEXT | NOT NULL |
| explanation | TEXT | NOT NULL |
| suggested_fix | TEXT | NULL |
| source_type | VARCHAR(30) | NULL |
| source_id | UUID | NULL |
| status | VARCHAR(30) | NOT NULL |
| created_at | TIMESTAMP | NOT NULL |

Categories:
FACTUAL_ERROR, TERMINOLOGY, TONE, UNSUPPORTED_CLAIM, ACCESSIBILITY.

Severity:
LOW, MEDIUM, HIGH, CRITICAL.

Finding status:
OPEN, ACCEPTED, REJECTED, RESOLVED, DISPUTED.

Source type:
BRAND_FACT, BRAND_TERM, GUIDELINE, AI_ANALYSIS.

### 2.9 approvals

Stores manager approval decisions.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| submission_id | UUID | Foreign Key |
| version_id | UUID | Foreign Key |
| reviewer_id | UUID | Foreign Key |
| decision | VARCHAR(30) | NOT NULL |
| comment | TEXT | NULL |
| created_at | TIMESTAMP | NOT NULL |

Decisions:
APPROVED, REJECTED, CHANGES_REQUESTED.

### 2.10 audit_events

Maintains important application activities.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| organization_id | UUID | Foreign Key |
| user_id | UUID | Foreign Key, NULL |
| submission_id | UUID | Foreign Key, NULL |
| action | VARCHAR(100) | NOT NULL |
| details | JSONB | NULL |
| created_at | TIMESTAMP | NOT NULL |

Examples:
- CONTENT_SUBMITTED
- REVIEW_COMPLETED
- CORRECTION_ACCEPTED
- APPROVAL_REQUESTED
- CONTENT_APPROVED

## 3. Relationships

- One organization can have multiple users.
- One organization can have multiple brand guidelines.
- One organization can have multiple brand facts.
- One organization can have multiple brand terms.
- One organization can have multiple submissions.
- One submission can have multiple content versions.
- One content version can have multiple findings.
- One submission can have multiple approval records.
- One organization can have multiple audit events.

## 4. Important Database Rules

1. Every organisation-specific record must be associated with its organization.
2. A user can only access data belonging to their organisation.
3. Original content must remain preserved.
4. Every revision creates a new content version.
5. Approval applies to a particular content version.
6. Findings must reference their corresponding content version.
7. AI findings and deterministic rule findings must follow the same data structure.
8. Database changes must be managed through Alembic migrations.

## 5. Initial Demo Data

Organisation: TechNova

Product: SmartWatch Pro

Approved facts:
- Product name: SmartWatch Pro
- Battery life: 24 hours
- Price: ₹1,499

Approved tone:
- Professional
- Friendly
- Informative

Prohibited claims:
- India's No. 1
- Guaranteed to transform your life

## 6. Implementation Status

This document defines the proposed database design.

The schema must be reviewed and approved before implementation.
# 7. Review Management

## 7.1 reviews

Stores individual analysis attempts performed on a content version.

| Column | Type | Constraints |
|---|---|---|
| id | UUID | Primary Key |
| version_id | UUID | Foreign Key |
| status | VARCHAR(30) | NOT NULL |
| total_findings | INTEGER | DEFAULT 0 |
| created_at | TIMESTAMP | NOT NULL |
| completed_at | TIMESTAMP | NULL |

Possible statuses:
- PENDING
- COMPLETED
- FAILED

## 7.2 Updated findings relationship

The findings table must reference review_id instead of directly referencing only version_id.

Every finding belongs to a specific review.

A content version can have multiple review attempts.

## 7.3 Review Rules

1. Every review belongs to one content version.
2. Every finding belongs to one review.
3. A new analysis creates a new review record.
4. Previous review results must be preserved.
5. Accepting a correction does not automatically resolve a finding.
6. After corrections, the system creates a new content version and performs a fresh review.
7. The latest completed review is used for the current compliance report.