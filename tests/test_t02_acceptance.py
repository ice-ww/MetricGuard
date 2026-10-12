import duckdb

from experiments.t02.acceptance import create_fixture


def test_independent_acceptance_fixture_has_hand_calculated_totals(tmp_path):
    database = create_fixture(tmp_path / "snapshot.duckdb")
    with duckdb.connect(str(database), read_only=True) as connection:
        assert connection.execute(
            "SELECT count(*), sum(amount) FROM sales"
        ).fetchall() == [(3, 37)]
        assert connection.execute(
            "SELECT name FROM regions ORDER BY id"
        ).fetchall() == [("East",), ("West",)]
