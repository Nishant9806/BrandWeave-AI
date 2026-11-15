"""
Prohibited Claim Checker

Detects unsupported marketing claims defined by the brand.
"""

import re

from .rules import PROHIBITED_CLAIMS


def check_claims(content: str) -> list[dict]:
    findings = []

    for rule in PROHIBITED_CLAIMS:
        claim = rule["claim"]

        pattern = re.compile(
            re.escape(claim),
            re.IGNORECASE
        )

        for match in pattern.finditer(content):
            findings.append({
                "category": "UNSUPPORTED_CLAIM",
                "severity": "HIGH",
                "confidence": 1.0,
                "original_text": match.group(0),
                "explanation": rule["explanation"],
                "suggested_fix": None,
                "source_type": "GUIDELINE",
                "source_id": claim,
                "status": "OPEN"
            })

    return findings
