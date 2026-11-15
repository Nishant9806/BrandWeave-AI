
from pydantic import BaseModel, Field
from typing import Optional


class ContentCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content_type: str = Field(default="ADVERTISEMENT", max_length=50)
    content: str = Field(..., min_length=1)


class ContentResponse(BaseModel):
    submission_id: str
    version_id: str
    version_number: int
    title: str
    content_type: str
    status: str


class FindingResponse(BaseModel):
    id: str
    category: str
    severity: str
    confidence: float
    original_text: str
    explanation: str
    suggested_fix: Optional[str] = None
    status: str


class ReviewResponse(BaseModel):
    review_id: str
    status: str
    total_findings: int
    findings: list[FindingResponse]

class ContentCorrection(BaseModel):
    content: str = Field(..., min_length=1)
