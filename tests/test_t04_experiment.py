import json

from experiments.t04.validation import run_experiment


def test_development_experiment_records_independent_references_and_frozen_rule(tmp_path):
    report = run_experiment(tmp_path / "run", seeds=[7], simulations=100)
    assert report["automatic_pass"]
    assert report["numeric_reference"]["comparisons"] == 64
    assert len(report["development"]) == 6
    assert report["frozen_rule"]["version"] == "t04-v1"
    insufficient = next(row for row in report["development"] if row["scenario"] == "insufficient")
    assert all(result["status"] == "insufficient_evidence" for result in insufficient["comparisons"].values())
    assert report["end_to_end_agent_false_positive_rate"] is None
    saved = json.loads((tmp_path / "run" / "report.json").read_text())
    assert saved["automatic_pass"] is True
