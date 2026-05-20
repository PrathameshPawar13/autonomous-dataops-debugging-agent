from app.graph.state import DebuggingState
from app.llm.ollama_client import call_ollama
from app.utils.json_parser import extract_json


def error_classifier_agent(state: DebuggingState) -> DebuggingState:
    prompt = f"""
You are a senior DataOps engineer.

Classify the following data pipeline failure into exactly one category.

Allowed categories:
- schema_drift
- sql_error
- permission_error
- connection_error
- timeout_error
- data_quality_error
- dependency_error
- resource_error
- unknown

Return only valid JSON in this exact format:
{{
  "error_type": "schema_drift",
  "confidence": 0.90,
  "reason": "short reason"
}}

Rules:
- If a column/table is missing or changed, use schema_drift.
- If privileges/access are missing, use permission_error.
- If task exceeded time, use timeout_error.
- If nulls/duplicates/expectations failed, use data_quality_error.
- If upstream task failed, use dependency_error.

Parsed log:
{state.parsed_log}

Raw log:
{state.raw_log}
"""

    response = call_ollama(prompt)

    try:
        result = extract_json(response)
        state.error_type = result.get("error_type", "unknown")
        state.error_confidence = float(result.get("confidence", 0.0))
        state.classification_reason = result.get("reason", "")
    except Exception as exc:
        state.error_type = "unknown"
        state.error_confidence = 0.0
        state.classification_reason = f"Failed to parse classifier response: {exc}"

    state.messages.append(f"Classifier Agent: classified error as {state.error_type}.")

    return state
