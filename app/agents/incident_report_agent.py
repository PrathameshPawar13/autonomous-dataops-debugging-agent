from app.graph.state import DebuggingState
from app.llm.ollama_client import call_ollama


def incident_report_agent(state: DebuggingState) -> DebuggingState:
    prompt = f"""
You are a senior data engineering incident manager.

Create a professional incident report for this pipeline failure.

Use this structure:

# Incident Report

## 1. Incident Summary
## 2. Error Classification
## 3. Root Cause
## 4. Recommended Fix
## 5. Prevention Steps
## 6. Severity
## 7. Suggested Owner
## 8. Next Actions

Context:

Raw log:
{state.raw_log}

Parsed log:
{state.parsed_log}

Error type:
{state.error_type}

Confidence:
{state.error_confidence}

Classification reason:
{state.classification_reason}

Root cause:
{state.root_cause}

Fix recommendation:
{state.fix_recommendation}

Validation status:
{state.validation_status}

Validation feedback:
{state.validation_feedback}
"""

    state.incident_report = call_ollama(prompt).strip()
    state.messages.append("Incident Report Agent: generated final incident report.")

    return state
