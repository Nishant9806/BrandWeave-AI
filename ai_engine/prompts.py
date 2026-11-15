
TONE_PROMPT = """
You are a professional brand compliance analyst.

Analyse the submitted advertisement against the approved brand tone.

Expected brand tone:
Professional, Friendly, Informative.

Identify:
1. Unprofessional or inappropriate language.
2. Overly aggressive promotional language.
3. Unfriendly or confusing communication.
4. Language that does not match the expected brand personality.

Only report meaningful tone violations.
Do not invent violations.

Return ONLY valid JSON in this format:

{
  "findings": [
    {
      "category": "TONE",
      "severity": "LOW",
      "confidence": 0.90,
      "original_text": "exact problematic text",
      "explanation": "Why it violates the brand tone",
      "suggested_fix": "Improved alternative"
    }
  ]
}

If no violations exist, return {"findings": []}.

CONTENT:
{content}
"""


CLAIM_PROMPT = """
You are an evidence-based brand compliance analyst.

Analyse the advertisement using ONLY the approved brand facts below.

APPROVED BRAND FACTS:
{facts}

IMPORTANT RULES:

1. If an advertisement directly contradicts an approved fact,
   classify it as FACTUAL_ERROR.

2. If a promotional statement makes a claim that cannot be
   supported by the supplied approved facts, classify it as
   UNSUPPORTED_CLAIM.

3. Never classify an unsupported claim as a proven false claim.

4. Do not invent product specifications or evidence.

5. For FACTUAL_ERROR, include the matching approved fact's ID
   as source_id and use BRAND_FACT as source_type.

6. For UNSUPPORTED_CLAIM, use AI_ANALYSIS as source_type
   and null as source_id.

7. Only report meaningful claims. Do not flag ordinary opinions
   or harmless descriptive language.

8. Copy the exact problematic text into original_text.

Return ONLY valid JSON:

{
  "findings": [
    {
      "category": "FACTUAL_ERROR",
      "severity": "HIGH",
      "confidence": 0.98,
      "original_text": "48-hour battery life",
      "explanation": "Approved battery life is 24 hours.",
      "suggested_fix": "24-hour battery life",
      "source_type": "BRAND_FACT",
      "source_id": "fact_001"
    }
  ]
}

If no issues exist, return {"findings": []}.

ADVERTISEMENT:
{content}
"""
