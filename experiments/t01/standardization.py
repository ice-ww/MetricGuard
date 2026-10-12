"""A4 reference derived quantity, only for the complete fixed experiment windows."""

from pathlib import Path

import duckdb

from .references import Metric, python_metrics, records


def sql_standardization(database: Path) -> Metric:
    cohort = Path(__file__).with_name("cohort.sql").read_text()
    baseline = cohort.replace("$start", "$baseline_start").replace("$end", "$current_start")
    current = cohort.replace("$start", "$current_start")
    with duckdb.connect(str(database), read_only=True) as con:
        systems = records(con, f"""WITH baseline AS ({baseline}), current AS ({current}),
            b AS (SELECT os,count(*) AS baseline_users FROM baseline GROUP BY os),
            c AS (SELECT os,count(*) AS current_users,avg(retained::INTEGER) AS current_retention FROM current GROUP BY os)
            SELECT os,baseline_users,baseline_users/sum(baseline_users) OVER() AS baseline_share,
                current_users,current_users/sum(current_users) OVER() AS current_share,current_retention,
                sum(baseline_users*current_retention) OVER()/sum(baseline_users) OVER() AS standardized,
                sum(current_users*current_retention) OVER()/sum(current_users) OVER() AS actual
            FROM b FULL JOIN c USING(os) ORDER BY os""",
            {"baseline_start": "2026-01-01", "current_start": "2026-01-08", "end": "2026-01-15"})
    standardized, actual = systems[0]["standardized"], systems[0]["actual"]
    for row in systems:
        del row["standardized"], row["actual"]
    return {"systems": systems, "standardized_retention": standardized, "actual_retention": actual}


def python_standardization(database: Path) -> Metric:
    before = python_metrics(database, "2026-01-01", "2026-01-08")["retention"]
    current = python_metrics(database, "2026-01-08", "2026-01-15")["retention"]
    base_total = sum(r["users"] for r in before)
    total = sum(r["users"] for r in current)
    systems = []
    standardized = 0.0
    for os in sorted({r["os"] for r in before}):
        base = sum(r["users"] for r in before if r["os"] == os)
        n = sum(r["users"] for r in current if r["os"] == os)
        retained = sum(r["retained"] for r in current if r["os"] == os)
        standardized += base/base_total * retained/n
        systems.append({"os": os, "baseline_users": base, "baseline_share": base/base_total,
                        "current_users": n, "current_share": n/total, "current_retention": retained/n})
    return {"systems": systems, "standardized_retention": standardized,
            "actual_retention": sum(r["retained"] for r in current)/total}
