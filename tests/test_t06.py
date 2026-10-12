from experiments.t06 import retrieve


def test_exact_alias_adopts_inspectable_definition():
    result = retrieve("新用户次日留存", window=("2026-01-01", "2026-01-08"))
    assert result["status"] == "adopt"
    assert result["definition"]["id"] == "retention"
    assert "Asia/Shanghai" in result["definition"]["time"]
    assert result["method"] == "exact"


def test_real_business_ambiguity_never_silently_defaults_to_new_users():
    assert retrieve("留存率", window=("2026-01-01", "2026-01-08"))["reason"] == "retention_population_required"
    assert retrieve("24小时留存", window=("2026-01-01", "2026-01-08"))["status"] == "unsupported"


def test_saved_development_verification_queries():
    import json
    from pathlib import Path
    queries = json.loads(Path("experiments/t06/development_queries.json").read_text(encoding="utf-8-sig"))
    for query in queries:
        result = retrieve(query["query"], window=query.get("window", ("2026-01-01", "2026-01-08")))
        assert result["status"] == query["status"], query
        assert (result["definition"]["id"] if result["definition"] else None) == query["id"], query
        assert len(result["candidates"]) == 3


def test_time_population_and_unsupported_horizon_boundaries():
    window = ("2026-01-01", "2026-01-08")
    assert retrieve("新增用户30日留存", window)["status"] == "unsupported"
    assert retrieve("新增用户留存", window)["reason"] == "retention_horizon_required"
    assert retrieve("完播率", ("2026-01-01", "2026-01-08", "2026-01-09"))["status"] == "clarify"


def test_actual_experiment_reproduces_locked_configuration_and_independent_scores(tmp_path):
    from experiments.t06.experiment import run
    result = run(tmp_path / "run")
    assert result["passed"]
    assert len(result["reference_checks"]) == 56
    assert all(r["passed"] for r in result["results"])


def test_generic_materials_include_all_definition_fields_and_no_answers():
    from experiments.t06 import CORPUS
    import json
    import re
    required = {"name", "aliases", "definition", "numerator", "denominator", "dimensions", "joins", "time", "pitfalls"}
    assert all(required <= d.keys() and all(d[k] for k in required) for d in CORPUS)
    assert not re.search(r"A[1-8]|黄金答案|注入参数|预期路径|scenario|seed", json.dumps(CORPUS, ensure_ascii=False))
