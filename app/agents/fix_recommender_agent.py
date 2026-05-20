from app.graph.state import DebuggingState
from app.llm.ollama_client import call_ollama


def fix_recommender_agent(state: DebuggingState) -> DebuggingState:
    prompt = f"""
You are a senior DataOps engineer.

Recommend a practical fix for this pipeline failure.

Return the answer with these headings:
1. Immediate Fix
2. Long-Term Prevention
3. Suggested Owner
4. Severity

Error type:
{state.error_type}

Root cause:
{state.root_cause}

Parsed log:
{state.parsed_log}

Raw log:
{state.raw_log}
"""

    state.fix_recommendation = call_ollama(prompt).strip()
    state.messages.append("Fix Recommendation Agent: generated fix recommendation.")

    return state
