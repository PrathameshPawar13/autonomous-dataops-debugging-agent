from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class DebuggingState(BaseModel):
    raw_log: str

    parsed_log: Optional[Dict[str, Any]] = None

    error_type: Optional[str] = None
    error_confidence: Optional[float] = None
    classification_reason: Optional[str] = None

    root_cause: Optional[str] = None
    fix_recommendation: Optional[str] = None

    validation_status: Optional[str] = None
    validation_feedback: Optional[str] = None

    incident_report: Optional[str] = None

    retry_count: int = 0
    max_retries: int = 2

    messages: List[str] = Field(default_factory=list)
