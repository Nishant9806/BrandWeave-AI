
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

    if not content or not content.strip():
        return {
            "status": "FAILED",
            "total_findings": 0,
            "findings": [],
            "message": "Content cannot be empty."
        }

    factual_findings = check_facts(content)
    terminology_findings = check_terminology(content)
    claim_findings = check_claims(content)

    all_findings = (
        factual_findings
        + terminology_findings
        + claim_findings
    )

    return {
        "status": "COMPLETED",
        "total_findings": len(all_findings),
        "findings": all_findings
    }
