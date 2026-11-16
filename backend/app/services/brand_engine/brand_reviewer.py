"""
Brand Reviewer

Coordinates all deterministic brand checks
and combines their findings.
"""

from .fact_checker import check_facts
from .terminology_checker import check_terminology
from .claim_checker import check_claims


def review_brand_content(content: str) -> dict:
    """
    Run all deterministic brand checks on submitted content.
    """

    # --------------------------------------------------
    # 1. EMPTY CONTENT VALIDATION
    # --------------------------------------------------

    if not content or not content.strip():
        return {
            "status": "FAILED",
            "total_findings": 0,
            "findings": [],
            "message": "Content cannot be empty."
        }

    # --------------------------------------------------
    # 2. RUN INDIVIDUAL CHECKERS
    # --------------------------------------------------

    factual_findings = check_facts(content)

    terminology_findings = check_terminology(content)

    claim_findings = check_claims(content)

    # --------------------------------------------------
    # 3. COMBINE ALL FINDINGS
    # --------------------------------------------------

    all_findings = (
        factual_findings
        + terminology_findings
        + claim_findings
    )

    # --------------------------------------------------
    # 4. RETURN REVIEW RESULTS
    # --------------------------------------------------

    return {
        "status": "COMPLETED",
        "total_findings": len(all_findings),
        "findings": all_findings
    }