from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Text, Float, DateTime

Base = declarative_base()


class DebuggingRun(Base):
    __tablename__ = "debugging_runs"

    id = Column(Integer, primary_key=True, index=True)
    raw_log = Column(Text)
    error_type = Column(String)
    error_confidence = Column(Float)
    classification_reason = Column(Text)
    root_cause = Column(Text)
    fix_recommendation = Column(Text)
    validation_status = Column(String)
    validation_feedback = Column(Text)
    incident_report = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
