import os
import streamlit as st

from app.graph.state import DebuggingState
from app.graph.workflow import build_debugging_graph
from app.reports.report_writer import save_markdown_report
from app.database.db import save_debugging_run, init_db


st.set_page_config(
    page_title="Autonomous DataOps Debugging Agent",
    layout="wide"
)

init_db()

st.title("Autonomous DataOps Debugging Agent")
st.write(
    "Analyze failed Airflow, dbt, Snowflake, and data quality logs using a local multi-agent AI workflow."
)

sample_dir = "data/sample_logs"
sample_files = sorted([f for f in os.listdir(sample_dir) if f.endswith(".log")])

with st.sidebar:
    st.header("Options")
    selected_sample = st.selectbox("Load sample log", ["None"] + sample_files)

raw_log = ""

if selected_sample != "None":
    with open(os.path.join(sample_dir, selected_sample), "r", encoding="utf-8") as file:
        raw_log = file.read()

raw_log = st.text_area("Pipeline Failure Log", value=raw_log, height=300)

if st.button("Analyze Failure"):
    if not raw_log.strip():
        st.warning("Please paste or load a pipeline failure log.")
    else:
        with st.spinner("Agents are analyzing the failure..."):
            graph = build_debugging_graph()
            initial_state = DebuggingState(raw_log=raw_log)
            result = graph.invoke(initial_state)

        run_id = save_debugging_run(result)

        st.success(f"Analysis saved to database. Run ID: {run_id}")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Error Type", result.get("error_type", "unknown"))

        with col2:
            st.metric("Confidence", result.get("error_confidence", 0.0))

        with col3:
            st.metric("Validation", result.get("validation_status", "unknown"))

        st.subheader("Parsed Log")
        st.json(result.get("parsed_log"))

        st.subheader("Classification Reason")
        st.write(result.get("classification_reason"))

        st.subheader("Root Cause")
        st.write(result.get("root_cause"))

        st.subheader("Fix Recommendation")
        st.markdown(result.get("fix_recommendation"))

        st.subheader("Validation Feedback")
        st.write(result.get("validation_feedback"))

        st.subheader("Incident Report")
        st.markdown(result.get("incident_report"))

        report_path = save_markdown_report(result.get("incident_report", ""))

        with open(report_path, "rb") as file:
            st.download_button(
                label="Download Incident Report",
                data=file,
                file_name=os.path.basename(report_path),
                mime="text/markdown",
            )

        st.subheader("Agent Trace")
        for msg in result.get("messages", []):
            st.write("- " + msg)
