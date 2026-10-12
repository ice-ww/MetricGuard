"""Approved result boundary: independently fixed size expectations."""

import duckdb

from experiments.t02.limits import bounded_result


def test_small_reference_query_keeps_exact_values():
    with duckdb.connect() as con:
        result = bounded_result(con.execute("SELECT 7 AS n, '杭州' AS city UNION ALL SELECT 9, NULL"))
    assert result["status"] == "ok"
    assert result["rows"] == [[7, "杭州"], [9, None]]
    assert result["truncated"] is False


def test_thousand_row_limit_is_explicit_and_preserves_reference_prefix():
    with duckdb.connect() as con:
        result = bounded_result(con.execute("SELECT i FROM range(1002) t(i) ORDER BY i"))
    assert result["status"] == "ok"
    assert len(result["rows"]) == 1000
    assert result["rows"][0] == [0]
    assert result["rows"][-1] == [999]
    assert result["truncated"] is True


def test_oversized_single_cell_returns_no_partial_evidence():
    with duckdb.connect() as con:
        result = bounded_result(con.execute("SELECT repeat('x', 65537)"))
    assert result["status"] == "output_limit"
    assert result["limit"] == "cell_bytes"
    assert "rows" not in result


def test_escaped_multibyte_wire_size_is_bounded():
    with duckdb.connect() as con:
        result = bounded_result(con.execute("SELECT repeat('杭', 12000)"))
    assert result["status"] == "output_limit"


def test_aggregate_bytes_limit_and_width_limit():
    with duckdb.connect() as con:
        result = bounded_result(con.execute("SELECT repeat('x', 60000) FROM range(20)"))
        wide = bounded_result(con.execute("SELECT " + ",".join("1" for _ in range(65))))
    assert result["status"] == "output_limit"
    assert result["limit"] == "result_bytes"
    assert "rows" not in result
    assert wide["status"] == "output_limit"
    assert wide["limit"] == "columns"
