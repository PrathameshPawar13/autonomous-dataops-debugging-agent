# Error Taxonomy

The agent classifies pipeline failures into the following categories:

## 1. schema_drift
- Missing column
- Renamed column
- Changed data type
- Missing table

## 2. sql_error
- Syntax error
- Invalid identifier
- Failed join
- Aggregation issue

## 3. permission_error
- Missing database permission
- Missing schema access
- Role-based access issue

## 4. connection_error
- API unavailable
- Database connection failed
- Network issue

## 5. timeout_error
- Long-running query
- DAG timeout
- Task exceeded execution time

## 6. data_quality_error
- Null threshold exceeded
- Duplicate records
- Row count mismatch
- Freshness failure

## 7. dependency_error
- Upstream task failed
- Missing dependency
- dbt model dependency issue

## 8. resource_error
- Warehouse overloaded
- Memory issue
- Compute limit exceeded

## 9. unknown
- Error cannot be confidently classified
