# Evaluation

The MVP is evaluated on five synthetic but realistic pipeline failure logs.

| Log File | Expected Error Type | Agent Output | Correct? |
|---|---|---|---|
| dbt_column_missing.log | schema_drift | TBD | TBD |
| timeout_error.log | timeout_error | TBD | TBD |
| snowflake_permission_error.log | permission_error | TBD | TBD |
| data_quality_error.log | data_quality_error | TBD | TBD |
| dependency_error.log | dependency_error | TBD | TBD |

## Evaluation Criteria

The agent output is considered correct if:
1. The error category matches the expected failure class.
2. The root cause references the actual failing component.
3. The fix recommendation is actionable.
4. The validation agent marks the output as valid or gives useful feedback.
