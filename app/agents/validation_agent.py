from app.graph.state import DebuggingState
from app.llm.ollama_client import call_ollama
from app.utils.json_parser import extract_json


def validation_agent(state: DebuggingState) -> DebuggingState:
    prompt = f"""
You are a strict DataOps validation agent.

Evaluate whether the root cause and fix recommendation are useful.

Check:
- Is the error type consistent with the log?
- Is the root cause specific?
- Is the fix actionable?
- Is the recommendation aligned with the error type?

Return only valid JSON:
{{
  "status": "valid",
  "feedback": "short explanation"
}}

Use status "valid" only if the analysis is useful.
Use status "invalid" if it is generic, off-topic, or not actionable.

Raw log:
{state.raw_log}

Error type:
{state.error_type}

Root cause:
{state.root_cause}

Fix recommendation:
{state.fix_recommendation}
"""

    response = call_ollama(prompt)

    try:
        result = extract_json(response)
        state.validation_status = result.get("status", "invalid")
        state.validation_feedback = result.get("feedback", "")
    except Exception as exc:
        state.validation_status = "invalid"
        state.validation_feedback = f"Could not parse validation response: {exc}"

    state.messages.append(f"Validation Agent: status = {state.validation_status}.")

    return state
