from app.graph.state import DebuggingState
from app.llm.ollama_client import call_ollama


def root_cause_agent(state: DebuggingState) -> DebuggingState:
    prompt = f"""
You are a senior data engineering incident investigator.

Given the pipeline log and classified error type, identify the most likely root cause.

Be specific. Mention the affected DAG/task/model/table/column if available.

Error type:
{state.error_type}

Classification reason:
{state.classification_reason}

Parsed log:
{state.parsed_log}

Raw log:
{state.raw_log}

Write a concise root cause explanation in 2-4 sentences.
"""

    state.root_cause = call_ollama(prompt).strip()
    state.messages.append("Root Cause Agent: generated root cause analysis.")

    return state
