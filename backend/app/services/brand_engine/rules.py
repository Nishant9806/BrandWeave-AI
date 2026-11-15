"""
TechNova Brand Configuration

This file contains the approved brand information and governance
rules used by the Brand Intelligence Engine.

All rule-based checks should refer to this configuration.
"""

# --------------------------------------------------
# 1. BRAND INFORMATION
# --------------------------------------------------

BRAND_PROFILE = {
    "brand_name": "TechNova",
    "product_name": "SmartWatch Pro",
    "industry": "Technology",
    "description": "Technology brand focused on smart devices."
}


# --------------------------------------------------
# 2. APPROVED BRAND FACTS
# --------------------------------------------------

APPROVED_FACTS = {
    "battery_life": {
        "value": "24 hours",
        "description": "Approved battery life of SmartWatch Pro."
    },

    "price": {
        "value": "INR 1,499",
        "description": "Approved selling price of SmartWatch Pro."
    }
}


# --------------------------------------------------
# 3. TERMINOLOGY RULES
# --------------------------------------------------

TERMINOLOGY_RULES = {

    "prohibited_terms": [
        {
            "term": "Smart Watch Professional",
            "replacement": "SmartWatch Pro",
            "explanation": "Use the officially approved product name."
        }
    ],

    "preferred_terms": [
        {
            "term": "SmartWatch Pro",
            "explanation": "Use the official product name consistently."
        }
    ]
}


# --------------------------------------------------
# 4. PROHIBITED MARKETING CLAIMS
# --------------------------------------------------

PROHIBITED_CLAIMS = [
    {
        "claim": "India's No. 1",
        "explanation": "Unverified superiority claim."
    },
    {
        "claim": "Guaranteed to transform your life",
        "explanation": "Unsupported guaranteed-benefit claim."
    }
]


# --------------------------------------------------
# 5. BRAND TONE GUIDELINES
# --------------------------------------------------

BRAND_TONE = {
    "required_tone": [
        "Professional",
        "Friendly",
        "Informative"
    ],

    "avoid_tone": [
        "Aggressive",
        "Misleading",
        "Exaggerated"
    ]
}