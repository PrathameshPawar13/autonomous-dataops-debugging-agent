# Evaluation

The MVP was evaluated on five synthetic but realistic pipeline failure logs covering common DataOps failure scenarios.

| Log File | Expected Error Type | Agent Output | Correct? | Notes |
|---|---|---|---|---|
| dbt_column_missing.log | schema_drift | schema_drift | Yes | Correctly identified missing/unauthorized column reference. |
| timeout_error.log | timeout_error | timeout_error | Yes | Correctly identified Airflow task timeout. |
| snowflake_permission_error.log | permission_error | permission_error | Yes | Correctly identified missing schema privileges. |
| data_quality_error.log | data_quality_error | data_quality_error | Yes | Correctly identified failed null-value expectation. |
| dependency_error.log | dependency_error | dependency_error | Yes | Correctly identified upstream task dependency failure. |

## Evaluation Criteria

The agent output is considered correct if:

1. The error category matches the expected failure class.
2. The root cause references the actual failing component.
3. The fix recommendation is actionable.
4. The validation agent marks the output as valid or gives useful feedback.

## Current MVP Result

The current MVP correctly classified 5 out of 5 sample logs.

```text
Classification Accuracy: 100% on synthetic evaluation set
