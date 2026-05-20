from app.graph.state import DebuggingState
from app.graph.workflow import build_debugging_graph


def run_debugging_agent(raw_log: str):
    graph = build_debugging_graph()
    initial_state = DebuggingState(raw_log=raw_log)
    final_state = graph.invoke(initial_state)
    return final_state


if __name__ == "__main__":
    sample_log_path = "data/sample_logs/dbt_column_missing.log"

    with open(sample_log_path, "r", encoding="utf-8") as file:
        raw_log = file.read()

    result = run_debugging_agent(raw_log)

    print("\n===== ERROR TYPE =====")
    print(result.get("error_type"))

    print("\n===== CONFIDENCE =====")
    print(result.get("error_confidence"))

    print("\n===== ROOT CAUSE =====")
    print(result.get("root_cause"))

    print("\n===== FIX RECOMMENDATION =====")
    print(result.get("fix_recommendation"))

    print("\n===== VALIDATION =====")
    print(result.get("validation_status"))
    print(result.get("validation_feedback"))

    print("\n===== INCIDENT REPORT =====\n")
    print(result.get("incident_report"))

    print("\n===== AGENT TRACE =====")
    for msg in result.get("messages", []):
        print("-", msg)
