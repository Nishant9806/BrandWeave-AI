# BrandWeave AI — API Contract

## 1. General Information

Backend: FastAPI

Communication: REST API

Data Format: JSON

Base URL (Development): http://localhost:8000

API Prefix: /api

## 2. Health Check

### GET /api/health

Checks whether the backend is operational.

Response:

{
  "status": "healthy",
  "service": "BrandWeave API"
}

## 3. Brand Vault APIs

### GET /api/brand

Returns organisation brand information.

### POST /api/brand/facts

Adds an approved brand fact.

Request:

{
  "fact_key": "battery_life",
  "fact_value": "24 hours",
  "status": "APPROVED"
}

### GET /api/brand/facts

Returns approved brand facts.

### POST /api/brand/terms

Adds a terminology entry.

Request:

{
  "term": "Smart Watch Professional",
  "term_type": "PROHIBITED",
  "replacement": "SmartWatch Pro",
  "explanation": "Use the officially approved product name."
}

### GET /api/brand/terms

Returns terminology entries.

## 4. Content APIs

### POST /api/content

Creates a new content submission.

Request:

{
  "title": "SmartWatch Advertisement",
  "content_type": "SOCIAL_POST",
  "content": "Our new smartwatch has 48-hour battery life!"
}

Response:

{
  "submission_id": "123",
  "version": 1,
  "status": "DRAFT"
}

### GET /api/content

Returns all content submissions.

### GET /api/content/{id}

Returns submission details.

## 5. Review APIs

### POST /api/content/{id}/review

Runs deterministic and AI-based analysis.

Response:

{
  "submission_id": "submission_001",
  "version_id": "version_001",
  "review_id": "review_001",
  "status": "COMPLETED",
  "total_findings": 2,
  "findings": []
}
Every review run creates a new record in the reviews table.
Each review belongs to one specific content version.
Findings generated during a review must reference that review.
Previous review results must remain available.
A failed review must be recorded with status FAILED.
### GET /api/content/{id}/findings

Returns findings from the latest completed review of the submission's latest reviewed version.

## 6. Common Finding Schema

Every finding must follow this structure:

{
  "finding_id": "finding_001",
  "review_id": "review_001",
  "category": "FACTUAL_ERROR",
  "severity": "HIGH",
  "confidence": 0.98,
  "original_text": "48-hour battery life",
  "explanation": "Approved battery life is 24 hours.",
  "suggested_fix": "24-hour battery life",
  "source_type": "BRAND_FACT",
  "source_id": "fact_001",
  "status": "OPEN"
}

The backend must validate that each source reference points to an existing record of the specified source type. If no valid evidence reference exists, the finding must not be presented as an evidence-confirmed conflict.

Allowed categories:
- FACTUAL_ERROR
- TERMINOLOGY
- TONE
- UNSUPPORTED_CLAIM
- ACCESSIBILITY

Allowed severity:
- LOW
- MEDIUM
- HIGH
- CRITICAL

Allowed status:
- OPEN 	Finding has not been addressed.
- ACCEPTED Creator accepts the suggested correction.
- REJECTED 	Creator rejects the suggested correction.
- RESOLVED 	A subsequent review confirms the issue is fixed.
- DISPUTED Creator disputes the finding.

Confidence must be between 0 and 1.

An unsupported claim must be distinguished from a contradicted claim.

Findings without valid evidence references must not be presented as evidence-confirmed conflicts.

## 7. Correction API

### POST /api/content/{id}/corrections

Applies selected corrections and creates a new content version.

Request:

{
  "version_id": "version_001",
  "corrections": [
    {
      "finding_id": "finding_001",
      "replacement_text": "24-hour battery life"
    }
  ]
}

Response:

{
  "submission_id": "submission_001",
  "new_version_id": "version_002",
  "version_number": 2,
  "status": "DRAFT",
  "message": "Corrections applied successfully. A new review is required."
}

Corrections must reference findings from the specified content version's review.
Applying corrections creates a new content version.
The original content version must never be overwritten.
Applying a correction does not automatically mark the original finding as resolved.
A new review must be performed to determine whether the issue has been resolved.
The original version must remain unchanged.

## 8. Approval API

### POST /api/content/{id}/decision

Request:

{
  "version_id": "version_002",
  "decision": "APPROVED",
  "comment": "Content reviewed and approved."
}
Response:
{
  "submission_id": "submission_001",
  "version_id": "version_002",
  "decision": "APPROVED",
  "message": "Content approved successfully."
}
Allowed decisions:
- APPROVED
- REJECTED
- CHANGES_REQUESTED

Approval must apply to a specific content version.

## 9. History API

### GET /api/content/{id}/history

Returns all content versions and their timestamps.

## 10. Analytics API

### GET /api/insights/overview

Returns basic dashboard statistics.

Example response:

{
  "total_submissions": 10,
  "approved": 6,
  "pending": 2,
  "changes_requested": 2,
  "total_findings": 25
}

## 11. Error Response Format

All API errors should follow:

{
  "detail": "A descriptive error message"
}

Use appropriate HTTP status codes:
- 200: Successful request
- 201: Resource created
- 400: Invalid request
- 401: Unauthenticated
- 403: Permission denied
- 404: Resource not found
- 422: Validation error
- 500: Internal server error

## 12. Integration Rules

1. Frontend communicates only through backend APIs.
2. AI and rule engines return the common Finding schema.
3. Backend combines findings into one review report.
4. Database IDs are used for source references.
5. Every content revision creates a new version.
6. Approval applies to a particular version.
7. API changes must be documented before implementation.
8. All modules must follow these agreed data structures.

## 13. Implementation Status

This document defines the initial API contract.

Backend and frontend developers must review and agree on the request and response formats before implementation.