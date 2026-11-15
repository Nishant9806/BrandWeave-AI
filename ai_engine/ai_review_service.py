from uuid import uuid4
from pydantic import ValidationError

from .schemas import Finding, ReviewResult
from .tone_analysis import analyze_tone
from .claim_detection import detect_claims


def review_content(
    content: str,
    approved_facts: list[dict],
    review_id: str
) -> ReviewResult:

    try:
        raw_findings = []

        raw_findings.extend(analyze_tone(content))

        raw_findings.extend(
            detect_claims(content, approved_facts)
        )

        findings = []

        for item in raw_findings:
            item["review_id"] = review_id
            findings.append(Finding(**item))

        return ReviewResult(
            status="COMPLETED",
            total_findings=len(findings),
            findings=findings
        )

    except (ValueError, ValidationError, KeyError) as error:
        raise RuntimeError(
            f"AI review failed: {error}"
        ) from error


def run_review(content: str, approved_facts: list[dict]):
    review_id = str(uuid4())

    result = review_content(
        content=content,
        approved_facts=approved_facts,
        review_id=review_id
    )

    return result.model_dump(mode="json")
