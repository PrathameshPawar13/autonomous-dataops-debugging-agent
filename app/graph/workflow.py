from langgraph.graph import StateGraph, END

from app.graph.state import DebuggingState
from app.agents.log_parser_agent import log_parser_agent
from app.agents.error_classifier_agent import error_classifier_agent
from app.agents.root_cause_agent import root_cause_agent
from app.agents.fix_recommender_agent import fix_recommender_agent
from app.agents.validation_agent import validation_agent
from app.agents.incident_report_agent import incident_report_agent


def should_retry_or_continue(state: DebuggingState) -> str:
    if state.validation_status == "valid":
        return "incident_report"

    if state.retry_count < state.max_retries:
        state.retry_count += 1
        state.messages.append(
            f"Workflow: validation failed. Retrying root cause and fix generation. Retry {state.retry_count}/{state.max_retries}."
        )
        return "root_cause"

    state.messages.append("Workflow: max retries reached. Proceeding to incident report.")
    return "incident_report"


def build_debugging_graph():
    graph = StateGraph(DebuggingState)

    graph.add_node("log_parser", log_parser_agent)
    graph.add_node("classifier", error_classifier_agent)
    graph.add_node("root_cause", root_cause_agent)
    graph.add_node("fix_recommender", fix_recommender_agent)
    graph.add_node("validator", validation_agent)
    graph.add_node("incident_report", incident_report_agent)

    graph.set_entry_point("log_parser")

    graph.add_edge("log_parser", "classifier")
    graph.add_edge("classifier", "root_cause")
    graph.add_edge("root_cause", "fix_recommender")
    graph.add_edge("fix_recommender", "validator")

    graph.add_conditional_edges(
        "validator",
        should_retry_or_continue,
        {
            "root_cause": "root_cause",
            "incident_report": "incident_report",
        },
    )

    graph.add_edge("incident_report", END)

    return graph.compile()
