import re


def tokenize(text: str) -> set[str]:
    text = text.lower().replace("_", " ")
    return set(re.findall(r"[a-z0-9]+", text))


def retrieve_facts(
    content: str,
    approved_facts: list[dict],
    top_k: int = 5
) -> list[dict]:

    content_tokens = tokenize(content)
    results = []

    for fact in approved_facts:
        searchable_text = (
            str(fact.get("fact_key", "")) + " " +
            str(fact.get("fact_value", ""))
        )

        fact_tokens = tokenize(searchable_text)

        overlap = content_tokens.intersection(fact_tokens)

        if overlap:
            results.append({
                "fact": fact,
                "score": len(overlap)
            })

    results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return [
        item["fact"]
        for item in results[:top_k]
    ]
