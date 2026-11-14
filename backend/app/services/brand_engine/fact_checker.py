"""
Fact Checker

Compares claims in submitted content against approved
brand facts and generates structured findings.
"""

import re

from .rules import APPROVED_FACTS


def check_facts(content: str) -> list[dict]:
    """
    Check submitted content against approved brand facts.

    Returns a list of factual findings.
    """

    findings = []

    # --------------------------------------------------
    # 1. BATTERY LIFE CHECK
    # --------------------------------------------------

    battery_pattern = r"(\d+)\s*[- ]?\s*hour(?:s)?(?:\s+of)?\s+battery\s+life"

    battery_matches = re.finditer(
        battery_pattern,
        content,
        re.IGNORECASE
    )

    approved_battery = APPROVED_FACTS["battery_life"]["value"]
    approved_battery_hours = int(
        re.search(r"\d+", approved_battery).group()
    )

    for match in battery_matches:

        claimed_hours = int(match.group(1))

        if claimed_hours != approved_battery_hours:

            findings.append({
                "category": "FACTUAL_ERROR",
                "severity": "HIGH",
                "confidence": 1.0,
                "original_text": match.group(0),
                "explanation": (
                    f"The approved battery life is "
                    f"{approved_battery}, but the submitted content "
                    f"claims {claimed_hours} hours."
                ),
                "suggested_fix": f"{approved_battery_hours}-hour battery life",
                "source_type": "BRAND_FACT",
                "source_id": "battery_life",
                "status": "OPEN"
            })

    # --------------------------------------------------
    # 2. PRICE CHECK
    # --------------------------------------------------

    approved_price = APPROVED_FACTS["price"]["value"]

    price_pattern = r"(?<![A-Za-z0-9])(?:₹|Rs\.?\s*|INR\s*)([\d,]+)(?!\w)"

    price_matches = re.finditer(
        price_pattern,
        content,
        re.IGNORECASE
    )

    approved_price_number = int(
        re.sub(r"\D", "", approved_price)
    )

    for match in price_matches:

        claimed_price = int(
            re.sub(r"\D", "", match.group(1))
        )

        if claimed_price != approved_price_number:

            findings.append({
                "category": "FACTUAL_ERROR",
                "severity": "HIGH",
                "confidence": 1.0,
                "original_text": match.group(0),
                "explanation": (
                    f"The approved product price is "
                    f"{approved_price}, but the submitted content "
                    f"mentions {match.group(0)}."
                ),
                "suggested_fix": approved_price,
                "source_type": "BRAND_FACT",
                "source_id": "price",
                "status": "OPEN"
            })

    return findings
