# BrandWeave AI - Product Demonstration Plan

## 1. Demonstration Objective

Demonstrate how BrandWeave AI checks marketing content against an organisation's approved brand guidelines, identifies violations, suggests corrections and enables human approval before publication.

**Organisation:** TechNova  
**Product:** SmartWatch Pro  
**Primary demonstration user:** Content Creator  
**Final reviewer:** Manager

## 2. Approved Brand Information

The following information will be configured in the TechNova Brand Vault.

| Category | Approved Information |
|---|---|
| Product Name | SmartWatch Pro |
| Battery Life | 24 hours |
| Price | ₹1,499 |
| Brand Tone | Professional, Friendly, Informative |
| Prohibited Claim | India's No. 1 |
| Prohibited Claim | Guaranteed to transform your life |

All content checks must use these approved values.

## 3. Demonstration Workflow

### Step 1: Brand Vault Setup

The Admin accesses the Brand Vault and views TechNova's approved brand information.

Expected result:
- Approved product facts are visible.
- Preferred and prohibited terminology is available.
- Brand tone guidelines are accessible.

### Step 2: Content Submission

The Creator submits a social media advertisement for SmartWatch Pro.

Title: SmartWatch Pro Launch Advertisement

Content:

"Introducing SmartWatch Pro, India's No. 1 smartwatch! Enjoy an incredible 48-hour battery life at just ₹1,299. This smartwatch is guaranteed to transform your life. Buy yours today!"

Expected result:
- Content is successfully submitted.
- A submission record and first content version are created.
- The submission can be opened for review.

### Step 3: Brand Compliance Analysis

The Creator selects the option to analyse the advertisement.

The system runs:
- Deterministic prohibited terminology checks.
- Approved fact verification.
- AI-powered tone analysis.
- Unsupported promotional claim analysis.

Expected result:

The review engine identifies the following issues:

| Issue | Category | Severity |
|---|---|---|
| "India's No. 1" | UNSUPPORTED_CLAIM | HIGH |
| "48-hour battery life" | FACTUAL_ERROR | HIGH |
| "₹1,299" | FACTUAL_ERROR | HIGH |
| "Guaranteed to transform your life" | UNSUPPORTED_CLAIM | HIGH |

The exact prohibited phrases must also be checked against the configured brand terminology rules.

Every finding must include:
- Original text
- Explanation
- Violated rule or evidence
- Suggested correction
- Severity
- Confidence
- Source type and source reference, where valid

An unsupported promotional claim must not be incorrectly presented as a confirmed factual contradiction.

### Step 4: Suggested Corrections

The system provides suggested corrections.

Example:

| Original Text | Suggested Correction |
|---|---|
| 48-hour battery life | 24-hour battery life |
| ₹1,299 | ₹1,499 |
| India's No. 1 smartwatch | Remove the unsupported ranking claim |
| Guaranteed to transform your life | Discover SmartWatch Pro's features |

The Creator can accept or reject suggestions and manually edit the content.

### Step 5: Revised Content

The Creator applies the corrections and submits the revised content for another review.

Expected result:
- A new content version is created.
- The original version remains unchanged.
- A new review record is created.
- The latest review results are displayed.
- Previous findings and review history remain accessible.

### Step 6: Manager Approval

The Manager opens the pending approval and reviews the revised content.

Available decisions:
- APPROVED
- REJECTED
- CHANGES_REQUESTED

The Manager can also provide a review comment.

Expected result:
- The decision is stored.
- The decision is associated with the specific content version.
- The submission status is updated.
- The activity is recorded.

## 4. Final Demonstration Outcome

The judge should be able to complete the entire workflow independently:

1. Open the TechNova demonstration workspace.
2. View approved brand information.
3. Submit a marketing advertisement.
4. Run brand compliance analysis.
5. View findings and their supporting evidence.
6. Apply suggested corrections.
7. Create a revised content version.
8. Submit the revised content for approval.
9. Approve or request changes as a Manager.
10. View the revision history.

## 5. Product Validation

The demonstration is successful only when the core workflow works through the deployed application without developer assistance.

The product must preserve original content, distinguish unsupported claims from verified factual conflicts, and keep the final approval decision under human control.

## 6. Important Implementation Notes

- Follow MVP_SCOPE.md, DATABASE_SCHEMA.md and API_CONTRACT.md.
- Use the agreed Common Finding Schema for all findings.
- Do not hardcode database source IDs in the demonstration.
- Source references must point to actual approved brand records.
- Every correction must create a new content version.
- Every new analysis must create a new review record.
- Approval must apply to a specific version.
- Do not claim that a feature is implemented until it has been tested.