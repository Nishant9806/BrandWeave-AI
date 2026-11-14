# BrandWeave AI - Acceptance Criteria

## 1. Purpose

This document defines the expected behaviour of the BrandWeave AI MVP. Each criterion must be tested before the product is considered ready for the Round 2 demonstration.

## 2. Brand Vault

- [ ] Admin can view TechNova brand information.
- [ ] Approved product name is SmartWatch Pro.
- [ ] Approved battery life is 24 hours.
- [ ] Approved price is ₹1,499.
- [ ] Approved brand tone is Professional, Friendly and Informative.
- [ ] Prohibited claims are available to the review engine.

## 3. Content Submission

- [ ] Creator can submit text content.
- [ ] Creator can provide a title and content type.
- [ ] A submission record is created successfully.
- [ ] The original content is saved as version 1.
- [ ] Submitted content can be retrieved.

## 4. Brand Compliance Review

- [ ] Creator can initiate a review.
- [ ] Prohibited terminology is detected.
- [ ] Incorrect approved product facts are detected.
- [ ] AI analyses brand tone.
- [ ] AI identifies unsupported promotional claims.
- [ ] Every review creates a separate review record.
- [ ] Findings follow the Common Finding Schema.
- [ ] Each finding includes its category, severity, confidence, original text and explanation.
- [ ] Suggested corrections are provided where appropriate.
- [ ] Evidence-confirmed conflicts reference valid brand records.
- [ ] Unsupported claims are distinguished from confirmed factual conflicts.

## 5. Correction Workflow

- [ ] Creator can accept a suggested correction.
- [ ] Creator can reject a suggested correction.
- [ ] Creator can manually edit content.
- [ ] Applying corrections creates a new content version.
- [ ] Original content remains unchanged.
- [ ] A new review is required after correction.
- [ ] Previous review results remain available.

## 6. Human Approval

- [ ] Manager can view content awaiting approval.
- [ ] Manager can approve content.
- [ ] Manager can reject content.
- [ ] Manager can request changes.
- [ ] Manager can add a review comment.
- [ ] Approval is associated with a specific content version.
- [ ] Submission status is updated correctly.

## 7. History and Dashboard

- [ ] User can view previous content versions.
- [ ] User can view version timestamps.
- [ ] Previous findings and review records are preserved.
- [ ] Basic submission statistics are available.
- [ ] Important actions are recorded in the audit history.

## 8. Deployment and Usability

- [ ] Application opens using the public project link.
- [ ] Core workflow works without developer assistance.
- [ ] Frontend communicates with backend APIs.
- [ ] API errors are displayed appropriately.
- [ ] No major workflow-breaking errors remain.

## 9. Final Acceptance Condition

The MVP is accepted when a judge can independently submit an advertisement, receive evidence-linked findings, apply corrections, create a new content version, and complete the manager approval workflow.

Only tested and functional features may be marked as completed.