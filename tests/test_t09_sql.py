import duckdb
from experiments.t02.policy import validate_sql

def test_business_query_shanghai_boundary_and_actual_metadata():
    from experiments.t02.limits import bounded_result
    sql = validate_sql("SELECT CAST(registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE) + 1 AS next_day FROM users", schema_profile="business")
    with duckdb.connect() as con:
        con.execute("CREATE TABLE users(user_id VARCHAR, registered_at TIMESTAMPTZ, registration_os VARCHAR, registration_version VARCHAR, channel VARCHAR)")
        con.execute("INSERT INTO users VALUES ('u', '2026-01-01 16:01:00+00', 'ios', 'v1', 'organic')")
        result = bounded_result(con.execute(sql))
    assert result['rows'] == [['2026-01-03']]
    assert result['columns'] == [{'name':'next_day', 'type':'DATE'}]
import pytest
from experiments.t02.policy import PolicyError
from experiments.t02.profiles import BUSINESS_SCHEMA, identify_profile

@pytest.mark.parametrize('sql', [
    "SELECT CAST(user_id AS INTEGER) FROM users",
    "SELECT registered_at AT TIME ZONE 'UTC' FROM users",
    "SELECT registered_at AT TIME ZONE channel FROM users",
    "SELECT * FROM sales", "SELECT * FROM duckdb_tables()",
    "SELECT * FROM read_csv('/etc/passwd')", "SELECT * FROM main.users",
    "SELECT * FROM users; SELECT 1", "DELETE FROM users",
])
def test_business_policy_rejects_unreviewed_sql(sql):
    with pytest.raises(PolicyError):
        validate_sql(sql, schema_profile='business')

def test_legacy_does_not_expand_its_permission_with_business_profile():
    with pytest.raises(PolicyError):
        validate_sql("SELECT CAST('2026-01-01' AS DATE)")
    with pytest.raises(PolicyError):
        validate_sql('SELECT * FROM users')

def test_exact_business_schema_selected_from_actual_database_metadata():
    from pathlib import Path
    with duckdb.connect() as con:
        con.execute(Path('experiments/t01/schema.sql').read_text())
        tables = con.execute('SELECT table_schema,table_name,table_type FROM information_schema.tables ORDER BY table_schema,table_name').fetchall()
        columns = con.execute('SELECT table_schema,table_name,column_name,data_type FROM information_schema.columns ORDER BY table_schema,table_name,ordinal_position').fetchall()
        assert identify_profile(tables, columns) == 'business'
        con.execute('ALTER TABLE users ADD COLUMN secret VARCHAR')
        changed = con.execute('SELECT table_schema,table_name,column_name,data_type FROM information_schema.columns ORDER BY table_schema,table_name,ordinal_position').fetchall()
        with pytest.raises(ValueError):
            identify_profile(tables, changed)

def test_duplicate_evidence_columns_rejected_and_metadata_bounded():
    from experiments.t02.limits import bounded_result
    with duckdb.connect() as con:
        duplicate = bounded_result(con.execute('SELECT 1 AS value, 2 AS Value'))
        huge = bounded_result(con.execute('SELECT 1 AS "' + ('a'*9000) + '"'))
    assert duplicate['status'] == 'output_limit'
    assert duplicate['limit'] == 'duplicate_columns'
    assert huge['status'] == 'output_limit'
    assert huge['limit'] == 'column_metadata'

def test_timestamp_evidence_has_actual_type_and_json_scalar():
    from experiments.t02.limits import bounded_result
    with duckdb.connect() as con:
        con.execute("SET TimeZone='UTC'")
        result = bounded_result(con.execute("SELECT TIMESTAMPTZ '2026-01-01 16:01:00+00' AS observed_at"))
    assert result['status'] == 'ok'
    assert result['columns'] == [{'name':'observed_at','type':'TIMESTAMP WITH TIME ZONE'}]
    assert result['rows'] == [['2026-01-01 16:01:00+00:00']]
