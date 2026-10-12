import duckdb
import pytest

from experiments.t02.policy import PolicyError, validate_sql


def test_approved_aggregate_join_has_independent_expected_result():
    sql = """WITH totals AS (
      SELECT region_id, SUM(amount) AS amount FROM sales GROUP BY region_id
    ) SELECT r.name, t.amount FROM totals t JOIN regions r ON t.region_id=r.id
      ORDER BY r.name"""
    with duckdb.connect() as con:
        con.execute("CREATE TABLE sales(id INTEGER,region_id INTEGER,amount INTEGER)")
        con.execute("CREATE TABLE regions(id INTEGER,name VARCHAR)")
        con.execute("INSERT INTO sales VALUES (1,1,10),(2,1,20),(3,2,7)")
        con.execute("INSERT INTO regions VALUES (1,'East'),(2,'West')")
        assert con.execute(validate_sql(sql)).fetchall() == [('East', 30), ('West', 7)]


@pytest.mark.parametrize("sql", [
    "SELECT * FROM sales", "SELECT s.* FROM sales s",
    'SELECT "AMOUNT" FROM "SaLeS"',
    "SELECT COUNT(DISTINCT region_id), COALESCE(SUM(amount), 0) FROM sales",
    "SELECT s.id FROM sales s WHERE EXISTS (SELECT 1 FROM regions r WHERE r.id=s.region_id)",
    "SELECT amount FROM (SELECT amount FROM sales) s WHERE amount > 10",
    "WITH sales AS (SELECT id FROM regions) SELECT * FROM sales",
    "SELECT CASE WHEN amount > 10 THEN amount ELSE 0 END FROM sales",
    "SELECT 1 /* a harmless ; comment */",
])
def test_reviewed_subset_and_case_normalization(sql):
    canonical = validate_sql(sql)
    assert validate_sql(canonical) == canonical


@pytest.mark.parametrize("sql", [
    "", ";", "SELECT 1; SELECT 2", "SELECT 1; --comment\n COPY sales TO 'out.csv'",
    "WITH hidden AS (SELECT * FROM secret) SELECT * FROM hidden",
    "WITH hidden AS (SELECT * FROM secret), secret AS (SELECT * FROM sales) SELECT * FROM hidden",
    "SELECT * FROM sales UNION SELECT * FROM secret",
    "WITH RECURSIVE x AS (SELECT 1 UNION ALL SELECT * FROM x) SELECT * FROM x",
    "SELECT * FROM read_csv('marker.csv')", "SELECT * FROM 'marker.csv'",
    "SELECT * FROM read_parquet('../marker.parquet')",
    "SELECT * FROM read_csv('https://example.invalid/marker.csv')",
    "SELECT * FROM information_schema.tables", "SELECT * FROM pg_catalog.pg_tables",
    "SELECT * FROM main.sales", "SELECT * FROM memory.main.sales",
    "SELECT main.sales.amount FROM sales",
    "SELECT * FROM query('SELECT * FROM secret')", "SELECT * FROM query_table('sales')",
    "SELECT * FROM duckdb_settings()", "SELECT current_setting('enable_external_access')",
    "SELECT secret_macro(id) FROM sales", "SELECT secret_udf(id) FROM sales",
    "SELECT * FROM python_dataframe", "SELECT * FROM range(10)",
    "INSTALL httpfs", "LOAD httpfs", "ATTACH 'marker.db' AS other",
    "COPY sales TO 'marker.csv'", "SET enable_external_access=true", "PRAGMA version",
    "CALL checkpoint()", "CREATE MACRO f(x) AS x", "DELETE FROM sales",
    "SELECT unknown_column FROM sales", "SELECT r.unknown_column FROM regions r",
    "SELECT id FROM sales s JOIN regions r ON s.region_id=r.id",
    "SELECT secret.x FROM sales", "SELECT (SELECT secret FROM regions) FROM sales",
])
def test_attack_and_unapproved_object_corpus_rejected(sql):
    with pytest.raises(PolicyError):
        validate_sql(sql)


@pytest.mark.parametrize("sql", [
    "SELECT '" + "x" * 8192 + "'",
    "SELECT " + "(" * 33 + "1" + ")" * 33,
    "SELECT " + ",".join("1" for _ in range(600)),
])
def test_sql_complexity_bounded(sql):
    with pytest.raises(PolicyError):
        validate_sql(sql)
