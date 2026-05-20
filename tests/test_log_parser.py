from app.parser.log_parser import parse_log


def test_parse_log_detects_missing_column_keywords():
    raw_log = "SQL compilation error: column customer_id does not exist"
    parsed = parse_log(raw_log)

    assert "column" in parsed["detected_keywords"]
    assert "does not exist" in parsed["detected_keywords"]


def test_parse_log_detects_airflow_dag_and_task():
    raw_log = """
    airflow.exceptions.AirflowTaskTimeout
    Task: extract_sales_data
    DAG: sales_ingestion_pipeline
    """
    parsed = parse_log(raw_log)

    assert parsed["task_name"] == "extract_sales_data"
    assert parsed["dag_name"] == "sales_ingestion_pipeline"
