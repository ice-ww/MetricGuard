"""Reproducible development calibration, independent reference and simulation evidence."""

import hashlib
import importlib.metadata
import json
import platform
from dataclasses import asdict
from itertools import product
from pathlib import Path
from typing import Any

import duckdb
import numpy as np
from statsmodels.stats.proportion import confint_proportions_2indep, proportion_confint  # type: ignore[import-untyped]

from experiments.t01 import build_snapshot
from experiments.t01.references import python_metrics, sql_metrics
from .statistics import BinarySample, FrozenRule, compare, compare_users, standardized


def numeric_reference() -> dict[str, Any]:
    cases = [(0, 1), (1, 1), (0, 10), (10, 10), (1, 2), (1, 10000), (9999, 10000), (40, 100)]
    max_error = 0.0
    results = []
    for current, reference in product(cases, cases):
        value = compare(BinarySample(*current), BinarySample(*reference), independent=True)
        expected_single = proportion_confint(*current, alpha=.05, method="wilson")
        expected_diff = confint_proportions_2indep(*current, *reference, method="newcomb", compare="diff", alpha=.05)
        assert value.current_interval is not None and value.difference_interval_pp is not None
        error = max(*(abs(x-float(y)) for x, y in zip(value.current_interval, expected_single)),
                    *(abs(x-100*float(y)) for x, y in zip(value.difference_interval_pp, expected_diff)))
        max_error = max(max_error, error)
        results.append({"current": current, "reference": reference, "interval_pp": value.difference_interval_pp,
                        "reference_interval_pp": [100*float(x) for x in expected_diff], "max_error": error})
    return {"comparisons": len(results), "maximum_absolute_error": max_error, "pass": max_error < 1e-10,
            "reference": "statsmodels explicit Wilson and newcomb/diff alpha=.05", "results": results}


def coverage_simulation(repetitions: int) -> list[dict[str, Any]]:
    """Fixed iid Bernoulli model simulations; no claim about adaptive diagnosis."""
    rng = np.random.default_rng(20261012)
    results = []
    for n, p in product((20, 100, 400), (0.0, .01, .5, .99, 1.0)):
        hits, widths = 0, []
        for x in rng.binomial(n, p, size=repetitions):
            value = compare(BinarySample(int(x), n), BinarySample(int(x), n), independent=True)
            assert value.current_interval is not None
            low, high = value.current_interval
            hits += int(low-1e-14 <= p <= high+1e-14)
            widths.append(100*(high-low))
        results.append({"method": "Wilson", "n": n, "p": p, "repetitions": repetitions,
                        "coverage": hits/repetitions, "mean_width_pp": sum(widths)/repetitions})
    for n1, n0, p1, p0 in ((20, 1000, .01, .5), (100, 100, .5, .5),
                           (400, 400, .3, .5), (20, 20, 0.0, 1.0)):
        hits, widths = 0, []
        for x1, x0 in zip(rng.binomial(n1, p1, size=repetitions), rng.binomial(n0, p0, size=repetitions)):
            value = compare(BinarySample(int(x1), n1), BinarySample(int(x0), n0), independent=True)
            assert value.difference_interval_pp is not None
            low, high = value.difference_interval_pp
            hits += int(low-1e-12 <= 100*(p1-p0) <= high+1e-12)
            widths.append(high-low)
        results.append({"method": "Newcombe", "n_current": n1, "n_reference": n0, "p_current": p1,
                        "p_reference": p0, "repetitions": repetitions, "coverage": hits/repetitions,
                        "mean_width_pp": sum(widths)/repetitions})
    return results


def _observations(database: Path, start: str, end: str) -> list[dict[str, Any]]:
    """Trusted T01 relational cohort query, excluding incomplete registration days."""
    query = Path("experiments/t01/cohort.sql").read_text()
    with duckdb.connect(str(database), read_only=True) as con:
        cursor = con.execute(query, {"start": start, "end": end})
        columns = [description[0] for description in cursor.description]
        return [dict(zip(columns, values)) for values in cursor.fetchall()]


def _stratum(rows: list[dict[str, Any]], *, channel: str | None = None,
             version: str | None = None, metric: str = "retained") -> list[tuple[str, bool]]:
    return [(row["user_id"], bool(row[metric])) for row in rows if row["os"] == "Android"
            and (channel is None or row["channel"] == channel)
            and (version is None or row["version"] == version)]


def run_experiment(output: Path, *, seeds: list[int] | None = None, simulations: int = 2000) -> dict[str, Any]:
    if simulations < 1:
        raise ValueError("Positive simulation repetitions required")
    seeds = [7, 19, 41] if seeds is None else seeds
    if not seeds or len(set(seeds)) != len(seeds):
        raise ValueError("Nonempty distinct development seeds required")
    output.mkdir(parents=True, exist_ok=False)
    numeric = numeric_reference()
    development: list[dict[str, Any]] = []
    candidates: dict[str, list[dict[str, Any]]] = {f"delta{delta}_width{width}": []
                                                for delta, width in product((3, 5, 8), (10, 15, 20))}
    for seed, scenario in product(seeds, ("normal", "A1", "A2", "A3", "A4", "insufficient")):
        snapshot = build_snapshot(output / "development" / f"case{len(development):03d}", scenario=scenario, seed=seed)
        periods = [("2026-01-01", "2026-01-08"), ("2026-01-08", "2026-01-15")]
        metrics = [sql_metrics(snapshot.database, start, end) for start, end in periods]
        independent_counts = all(value == python_metrics(snapshot.database, *period)
                                 for period, value in zip(periods, metrics))
        base, current = [_observations(snapshot.database, start, value["coverage"]["retention_end"])
                         for (start, _), value in zip(periods, metrics)]
        complete = all(value["coverage"]["retention_complete"] for value in metrics)
        # A1 mixes two marginal probabilities when versions are pooled; A2 mixes
        # paid/organic. Fixed strata avoid both mixtures and user overlap.
        designs = {
            "organic_retention": (_stratum(current, channel="organic", version="1.0"),
                                  _stratum(base, channel="organic"), "decrease"),
            "paid_retention": (_stratum(current, channel="paid", version="1.0"),
                               _stratum(base, channel="paid"), "decrease"),
            "new_version_retention": (_stratum(current, channel="organic", version="2.0"),
                                      _stratum(base, channel="organic"), "decrease"),
            "new_version_crash": (_stratum(current, version="2.0", metric="crashed"),
                                  _stratum(base, metric="crashed"), "increase"),
        }
        comparisons = {name: asdict(compare_users(a, b, independent=True, complete=complete,
                                                   rule=FrozenRule(direction=direction)))
                       for name, (a, b, direction) in designs.items()}
        for delta, width in product((3, 5, 8), (10, 15, 20)):
            values = {name: compare_users(a, b, independent=True, complete=complete,
                                         rule=FrozenRule(threshold_pp=delta, max_width_pp=width, direction=direction)).status
                      for name, (a, b, direction) in designs.items()}
            candidates[f"delta{delta}_width{width}"].append({"seed": seed, "scenario": scenario, "statuses": values})
        base_os = {os: sum(row["users"] for row in metrics[0]["retention"] if row["os"] == os) for os in ("Android", "iOS")}
        current_os = {os: BinarySample(sum(row["retained"] for row in metrics[1]["retention"] if row["os"] == os),
                                      sum(row["users"] for row in metrics[1]["retention"] if row["os"] == os))
                      for os in ("Android", "iOS")}
        derived = standardized(base_os, current_os)
        if not complete:
            derived.update(status="insufficient_evidence", reason="incomplete_collection")
        development.append({"seed": seed, "scenario": scenario, "logical_hash": snapshot.logical_hash,
                            "independent_counts_agree": independent_counts, "comparisons": comparisons,
                            "standardized": derived, "coverage": [value["coverage"] for value in metrics]})
    summaries = {}
    for key, rows in candidates.items():
        normal = [status for row in rows if row["scenario"] == "normal" for status in row["statuses"].values()]
        expected = [row["statuses"][name] for row in rows for name in {
            "A1": ("new_version_retention", "new_version_crash"), "A2": ("paid_retention",),
            "A4": ("organic_retention", "paid_retention", "new_version_retention")
        }.get(row["scenario"], ())]
        all_statuses = [status for row in rows for status in row["statuses"].values()]
        summaries[key] = {"normal_comparisons": len(normal), "false_anomalies": normal.count("anomaly_supported"),
                          "normal_below_standard": normal.count("below_anomaly_standard"),
                          "normal_insufficient_or_indeterminate": sum(s != "below_anomaly_standard" and s != "anomaly_supported" for s in normal),
                          "target_comparisons": len(expected), "target_supported": expected.count("anomaly_supported"),
                          "insufficient_or_indeterminate": sum(s.startswith("insufficient") or s == "indeterminate" for s in all_statuses),
                          "total_comparisons": len(all_statuses), "results": rows}
    code_hashes = {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in (
        Path(__file__), Path(__file__).with_name("statistics.py"), Path("experiments/t01/cohort.sql"),
        Path("experiments/t01/snapshots.py"), Path("experiments/t01/references.py"))}
    chosen = summaries["delta5_width20"]
    checks = {
        "independent_numeric_reference": bool(numeric["pass"]),
        "independent_reference_queries": all(row["independent_counts_agree"] for row in development),
        "normal_no_false_anomaly": chosen["false_anomalies"] == 0,
        "development_target_supported": chosen["target_supported"] == chosen["target_comparisons"],
        "incomplete_never_no_anomaly": all(result["status"] == "insufficient_evidence" and result["difference_interval_pp"] is None
                                            for row in development if row["scenario"] == "insufficient"
                                            for result in row["comparisons"].values()),
        "derived_quantities_no_binomial_interval": all(row["standardized"]["interval"] is None for row in development),
    }
    report = {
        "automatic_pass": all(checks.values()), "checks": checks,
        "purpose": "development_calibration_only_not_frozen_acceptance", "seeds": seeds,
        "environment": {"python": platform.python_version(), "platform": platform.platform(),
                        **{name: importlib.metadata.version(name) for name in ("duckdb", "statsmodels", "numpy", "scipy")}},
        "numeric_reference": numeric, "development": development, "candidate_rules": summaries,
        "frozen_rule": {**asdict(FrozenRule()), "crash_direction": "increase", "state": "frozen_for_subsequent_validation",
                        "reason": "5 pp exploratory business tolerance; width <=20 pp preserves the 18 strong target effects in this development grid (15 pp retains 9), without new normal false anomalies. Normal uncertainty remains indeterminate; 8 pp loses 3 target comparisons, while 3 pp adds no target support. This is a development design choice, not universal business truth."},
        "code_hashes": code_hashes, "simulation": coverage_simulation(simulations),
        "end_to_end_agent_false_positive_rate": None,
        "limitations": ["No adaptive Agent exists in T04; full-workflow false-positive rate requires integration/T20.",
                        "Development seeds and fixed-parameter simulations are not unseen evaluation.",
                        "Independent homogeneous Bernoulli assumptions declared per fixed stratum, no day/device shocks.",
                        "A4 standardized and mixed OS totals descriptive only; A3 same-play telemetry comparison has no independent interval."]}
    (output / "report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return report
