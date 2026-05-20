import re
from typing import Dict, Any, List


def _detect_keywords(raw_log: str) -> List[str]:
    keywords = [
        "column",
        "does not exist",
        "not authorized",
        "timeout",
        "permission",
        "privileges",
        "null",
        "duplicate",
        "upstream",
        "dependency",
        "schema",
        "SQL compilation error",
        "access control",
        "failed with exception",
        "ValidationError",
        "AirflowTaskTimeout",
    ]

    found = []
    lower_log = raw_log.lower()

    for keyword in keywords:
        if keyword.lower() in lower_log:
            found.append(keyword)

    return found


def parse_log(raw_log: str) -> Dict[str, Any]:
    parsed = {
        "dag_name": None,
        "task_name": None,
        "model_name": None,
        "database": None,
        "schema": None,
        "table": None,
        "column": None,
        "error_message": raw_log[:1500],
        "detected_keywords": _detect_keywords(raw_log),
    }

    dag_match = re.search(r"DAG[:\s]+([A-Za-z0-9_\-]+)", raw_log, re.IGNORECASE)
    task_match = re.search(r"Task[:\s]+([A-Za-z0-9_\-]+)", raw_log, re.IGNORECASE)
    model_match = re.search(r"model\s+([A-Za-z0-9_\-]+)", raw_log, re.IGNORECASE)

    object_match = re.search(
        r"Object\s+'([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)'",
        raw_log,
        re.IGNORECASE,
    )

    schema_match = re.search(r"schema\s+([A-Za-z0-9_]+)", raw_log, re.IGNORECASE)

    column_match = re.search(r"Column:\s*([A-Za-z0-9_]+)", raw_log, re.IGNORECASE)

    if dag_match:
        parsed["dag_name"] = dag_match.group(1)

    if task_match:
        parsed["task_name"] = task_match.group(1)

    if model_match:
        parsed["model_name"] = model_match.group(1)

    if object_match:
        parsed["database"] = object_match.group(1)
        parsed["table"] = object_match.group(2)
        parsed["column"] = object_match.group(3)

    if schema_match:
        parsed["schema"] = schema_match.group(1)

    if column_match:
        parsed["column"] = column_match.group(1)

    return parsed
