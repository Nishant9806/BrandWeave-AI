import json
from ai_engine.ai_review_service import run_review

approved_facts = [
    {"id": "fact_001", "fact_key": "product_name", "fact_value": "SmartWatch Pro"},
    {"id": "fact_002", "fact_key": "battery_life", "fact_value": "24 hours"},
    {"id": "fact_003", "fact_key": "price", "fact_value": "₹1,499"}
]

advertisement = """
Introducing SmartWatch Pro!

Enjoy an incredible 48-hour battery life.
India's No. 1 smartwatch, guaranteed to transform your life!

Get yours today for just ₹1,499.
"""

if __name__ == "__main__":
    print("Starting BrandWeave AI Review...")

    result = run_review(
        content=advertisement,
        approved_facts=approved_facts
    )

    print("\n===== AI REVIEW RESULT =====")
    print(json.dumps(result, indent=4, ensure_ascii=False))
