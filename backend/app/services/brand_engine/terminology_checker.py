"""
Terminology Checker

Detects prohibited terminology and suggests
approved alternatives.
"""

import re

from .rules import TERMINOLOGY_RULES


def check_terminology(content: str) -> list[dict]:
    """
    Check submitted content for prohibited terminology.

    Returns a list of terminology findings.
    """

    findings = []

    prohibited_terms = TERMINOLOGY_RULES["prohibited_terms"]

    for rule in prohibited_terms:

        term = rule["term"]
        replacement = rule["replacement"]

        # Match the complete term, ignoring capitalization.
        pattern = re.compile(
            rf"(?<!\w){re.escape(term)}(?!\w)",
            re.IGNORECASE
        )

        matches = pattern.finditer(content)

        for match in matches:

            findings.append({
                "category": "TERMINOLOGY",
                "severity": "MEDIUM",
                "confidence": 1.0,
                "original_text": match.group(0),
                "explanation": rule["explanation"],
                "suggested_fix": replacement,
                "source_type": "BRAND_TERM",
                "source_id": term,
                "status": "OPEN"
            })

    return findings