# BrandWeave AI: Product Validation

## 1. Purpose

This document defines sample data and validation scenarios for testing the BrandWeave AI brand-governance workflow.

The objective is to verify that submitted content is checked against approved brand information, violations are explained, corrections can be applied, and final approval is handled by a human reviewer.

## 2. Demo Brand: TechNova

### Brand Identity

- **Brand:** TechNova
- **Product:** SmartWatch Pro
- **Industry:** Consumer Technology
- **Brand Tone:** Professional, Friendly, Informative

### Approved Product Facts

| Attribute | Approved Value |
|---|---|
| Product Name | SmartWatch Pro |
| Battery Life | 24 hours |
| Price | ₹1,499 |

### Brand Rules

- Product facts must match approved brand information.
- Unsupported superlative claims must be flagged.
- Guaranteed outcome claims must be flagged.
- Content should maintain a professional, friendly and informative tone.
- Product names and approved terminology should remain consistent.

### Prohibited Claims

- "India's No. 1"
- "Guaranteed to transform your life"

## 3. Sample Content A: Compliant Advertisement

**Title:** SmartWatch Pro Launch Advertisement

**Content:**

"Meet SmartWatch Pro by TechNova, designed to keep you connected throughout your day. Enjoy up to 24 hours of battery life at an affordable price of ₹1,499. Discover a smarter way to stay informed and connected with TechNova."

**Expected Result:**

- No factual conflicts with the approved product facts.
- No prohibited claims.
- Product name is consistent.
- Tone is professional, friendly and informative.
- The content should pass the review, subject to the actual engine's configured checks.

## 4. Sample Content B: Non-Compliant Advertisement

**Title:** SmartWatch Pro Promotional Advertisement

**Content:**

"Introducing SmartWatch Pro, India's No. 1 smartwatch! Enjoy an incredible 48-hour battery life at just ₹1,299. This smartwatch is guaranteed to transform your life. Buy yours today!"

### Expected Findings

| No. | Category | Severity | Problem | Expected Correction |
|---|---|---|---|---|
| 1 | UNSUPPORTED_CLAIM | HIGH | "India's No. 1" is not supported by approved brand evidence. | Remove the ranking claim. |
| 2 | FACTUAL_ERROR | HIGH | 48-hour battery life conflicts with the approved 24-hour specification. | Replace with 24 hours. |
| 3 | FACTUAL_ERROR | HIGH | ₹1,299 conflicts with the approved price of ₹1,499. | Replace with ₹1,499. |
| 4 | UNSUPPORTED_CLAIM | HIGH | "Guaranteed to transform your life" is prohibited. | Replace with a neutral product benefit. |

**Important:** The engine must distinguish unsupported claims from claims directly contradicted by approved facts.

## 5. Expected Corrected Advertisement

"Introducing SmartWatch Pro by TechNova! Enjoy an impressive 24-hour battery life at just ₹1,499. Stay connected and informed throughout your day with a smartwatch designed for your everyday needs."

The corrected content should undergo a fresh review rather than automatically clearing the previous findings.

## 6. Validation Scenarios

### Scenario 1: Brand Vault

- [ ] TechNova brand information is accessible.
- [ ] Approved product facts are displayed.
- [ ] Prohibited terminology is available to the review engine.

### Scenario 2: Content Submission

- [ ] Creator can submit advertisement content.
- [ ] Submission receives a unique identifier.
- [ ] Original content is preserved.

### Scenario 3: Automated Review

- [ ] Review runs against approved brand information.
- [ ] Factual conflicts are identified.
- [ ] Prohibited claims are flagged.
- [ ] Findings include category, severity, confidence and explanation.
- [ ] Findings reference valid evidence wherever applicable.

### Scenario 4: Correction Workflow

- [ ] Suggested corrections are displayed.
- [ ] Creator can accept or reject suggestions.
- [ ] Applying corrections creates a new content version.
- [ ] A fresh review can be performed on the revised version.
- [ ] Previous findings and versions remain available.

### Scenario 5: Human Approval

- [ ] Manager can review the revised content.
- [ ] Manager can approve, reject or request changes.
- [ ] The decision is associated with the correct content version.

### Scenario 6: History and Audit

- [ ] Previous content versions are accessible.
- [ ] Review results are preserved.
- [ ] Approval decisions are recorded.

## 7. Implementation Notes

1. This document defines expected product behaviour, not guaranteed engine output.
2. The backend must assign database IDs to brand facts, terminology entries, reviews and findings.
3. Expected findings must reference valid database evidence IDs at runtime. The sample scenarios do not assume fixed database IDs.
4. AI-generated findings and deterministic rule-engine findings must follow the common finding schema in `API_CONTRACT.md`.
5. Unsupported claims must not be presented as factually contradicted unless approved evidence establishes a contradiction.
6. A correction must create a new version. Existing versions and review results must never be overwritten.

## 8. Final Validation Goal

A judge should be able to open the deployed application, submit the non-compliant advertisement, inspect the findings, apply corrections, run a fresh review and complete the human approval workflow without developer assistance.