from typing import Optional, Literal
from pydantic import BaseModel, Field
from uuid import uuid4


Category = Literal[
    "FACTUAL_ERROR",
    "TERMINOLOGY",
    "TONE",
    "UNSUPPORTED_CLAIM",
    "ACCESSIBILITY"
]

Severity = Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]

FindingStatus = Literal[
    "OPEN", "ACCEPTED", "REJECTED", "RESOLVED", "DISPUTED"
]

SourceType = Literal[
    "BRAND_FACT", "BRAND_TERM", "GUIDELINE", "AI_ANALYSIS"
]


class Finding(BaseModel):
    finding_id: str = Field(default_factory=lambda: str(uuid4()))
    review_id: str
    category: Category
    severity: Severity
    confidence: float = Field(ge=0, le=1)
    original_text: str
    explanation: str
    suggested_fix: Optional[str] = None
    source_type: Optional[SourceType] = None
    source_id: Optional[str] = None
    status: FindingStatus = "OPEN"


class ReviewResult(BaseModel):
    status: Literal["COMPLETED", "FAILED"]
    total_findings: int
    findings: list[Finding]
