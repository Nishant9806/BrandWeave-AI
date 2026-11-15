import json
from .llm_client import generate_response
from .prompts import CLAIM_PROMPT
from .retrieval import retrieve_facts


def detect_claims(content: str, approved_facts: list[dict]) -> list[dict]:

    relevant_facts = retrieve_facts(
        content,
        approved_facts
    )

    facts = json.dumps(
        relevant_facts,
        ensure_ascii=False,
        indent=2
    )

    prompt = CLAIM_PROMPT.replace(
        "{content}", content
    ).replace(
        "{facts}", facts
    )

    response = generate_response(prompt)
    data = json.loads(response)

    return data.get("findings", [])
