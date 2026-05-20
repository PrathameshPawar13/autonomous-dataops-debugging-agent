# Autonomous DataOps Debugging Agent

An agentic AI system that analyzes failed Airflow, dbt, Snowflake, and data quality pipeline logs, identifies root causes, recommends fixes, validates the output, and generates professional incident reports.

The project is designed to demonstrate practical skills in Agentic AI, LangGraph workflows, DataOps automation, local LLMs, and production-style Python application development.

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

```text
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
