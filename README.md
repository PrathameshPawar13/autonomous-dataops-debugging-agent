# Autonomous DataOps Debugging Agent

An agentic AI system that analyzes failed **Airflow**, **dbt**, **Snowflake**, and **data quality** pipeline logs, identifies root causes, recommends fixes, validates the output, and generates professional incident reports.

The project demonstrates practical skills in **Agentic AI**, **LangGraph workflows**, **DataOps automation**, **local LLMs**, and production-style Python application development.

---

## Problem

Data engineering teams spend significant time manually debugging failed pipelines. Logs from Airflow, dbt, Snowflake, and data quality tools often contain useful signals, but identifying the actual root cause still requires manual investigation.

This project automates first-level incident analysis using a multi-agent AI workflow.

---

## Features

- Pipeline log parsing
- Error classification
- Root cause analysis
- Fix recommendation
- Validation and retry loop
- Incident report generation
- Streamlit dashboard
- SQLite storage
- Markdown report export
- Fully local LLM using Ollama

---

## Architecture

Pipeline Log  
↓  
Log Parser Agent  
↓  
Error Classifier Agent  
↓  
Root Cause Agent  
↓  
Fix Recommender Agent  
↓  
Validation Agent  
↓  
Retry if invalid  
↓  
Incident Report Agent  
↓  
Dashboard + Database + Export  

---

## Agent Workflow

| Agent | Role | Output |
|---|---|---|
| Log Parser Agent | Extracts structured information from raw logs | Parsed log fields and detected keywords |
| Error Classifier Agent | Classifies the pipeline failure type | Error category, confidence score, reason |
| Root Cause Agent | Determines the likely cause of failure | Root cause explanation |
| Fix Recommender Agent | Suggests immediate and long-term fixes | Actionable fix recommendation |
| Validation Agent | Checks whether the analysis is useful | Valid/invalid status and feedback |
| Incident Report Agent | Generates the final report | Professional incident report |

---

## Tech Stack

- Python
- LangGraph
- LangChain
- Ollama
- Llama 3.2 1B / Mistral
- Streamlit
- SQLite
- SQLAlchemy
- Pydantic
- pytest

---

## Screenshots

### Dashboard Home

![Dashboard Home](docs/screenshots/dashboard_home.png)

### Analysis Output

![Analysis Output](docs/screenshots/analysis_output.png)

### Agent Trace

![Agent Trace](docs/screenshots/agent_trace.png)

---

## Evaluation

The MVP was tested on five synthetic but realistic pipeline failure logs.

| Log File | Expected Error Type | Agent Output | Correct? |
|---|---|---|---|
| dbt_column_missing.log | schema_drift | schema_drift | Yes |
| timeout_error.log | timeout_error | timeout_error | Yes |
| snowflake_permission_error.log | permission_error | permission_error | Yes |
| data_quality_error.log | data_quality_error | data_quality_error | Yes |
| dependency_error.log | dependency_error | dependency_error | Yes |

Detailed evaluation is available in:

`docs/evaluation.md`

## Sample Logs

Sample logs are available in:

`data/sample_logs/`

Current examples include:

- dbt missing column error
- Airflow timeout error
- Snowflake permission error
- Data quality validation error
- Upstream dependency failure


## Project Structure

autonomous-dataops-debugging-agent/  
├── app/  
│   ├── agents/  
│   ├── graph/  
│   ├── llm/  
│   ├── parser/  
│   ├── database/  
│   ├── reports/  
│   ├── dashboard/  
│   ├── config/  
│   └── utils/  
├── data/  
│   ├── sample_logs/  
│   └── outputs/  
├── docs/  
│   ├── screenshots/  
│   └── evaluation.md  
├── tests/  
├── requirements.txt  
├── README.md  
├── Dockerfile  
└── main.py  

