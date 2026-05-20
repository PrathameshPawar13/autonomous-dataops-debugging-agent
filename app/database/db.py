from app.config.settings import DATABASE_URL
from app.database.models import Base, DebuggingRun
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def save_debugging_run(result: dict) -> int:
    init_db()

    session = SessionLocal()

    try:
        run = DebuggingRun(
            raw_log=result.get("raw_log"),
            error_type=result.get("error_type"),
            error_confidence=result.get("error_confidence"),
            classification_reason=result.get("classification_reason"),
            root_cause=result.get("root_cause"),
            fix_recommendation=result.get("fix_recommendation"),
            validation_status=result.get("validation_status"),
            validation_feedback=result.get("validation_feedback"),
            incident_report=result.get("incident_report"),
        )

        session.add(run)
        session.commit()
        session.refresh(run)

        return run.id

    finally:
        session.close()
