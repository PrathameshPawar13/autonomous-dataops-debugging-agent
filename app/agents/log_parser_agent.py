from app.graph.state import DebuggingState
from app.parser.log_parser import parse_log


def log_parser_agent(state: DebuggingState) -> DebuggingState:
    parsed = parse_log(state.raw_log)

    state.parsed_log = parsed
    state.messages.append("Log Parser Agent: parsed raw pipeline log.")

    return state
