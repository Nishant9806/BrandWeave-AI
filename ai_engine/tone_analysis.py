import json
from .llm_client import generate_response
from .prompts import TONE_PROMPT


def analyze_tone(content: str) -> list[dict]:
    prompt = TONE_PROMPT.replace("{content}", content)

    response = generate_response(prompt)
    data = json.loads(response)

    return data.get("findings", [])
