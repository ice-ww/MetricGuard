from __future__ import annotations

import hashlib
import json
import platform
import sys
import unicodedata
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Any

from .retrieval import CONFIG, CORPUS, ROOT, rank, retrieve


def reference_tokens(text: str, mode: str) -> list[str]:
    """Independent scanner, no production regex/tokenizer dependency."""
    tokens: list[str] = []
    runs: list[tuple[str, str]] = []
    for char in unicodedata.normalize("NFKC", text).lower():
        kind = "han" if "\u4e00" <= char <= "\u9fff" else "latin" if char.isascii() and (char.isalnum() or char == "_") else "separator"
        if kind == "separator":
            runs.append((kind, ""))
        elif runs and runs[-1][0] == kind:
            runs[-1] = (kind, runs[-1][1] + char)
        else:
            runs.append((kind, char))
    for kind, word in runs:
        if kind == "han":
            tokens.extend(list(word) if mode == "unigram" else [a + b for a, b in zip(word, word[1:])])
        elif kind == "latin":
            tokens.append(word)
    return tokens


def reference_rank(query: str, mode: str) -> list[dict[str, Any]]:
    """50-digit Decimal BM25 with document-term incidence; no rank/tokenize calls."""
    texts = [" ".join([d["name"], *d["aliases"], d["definition"]]) for d in CORPUS]
    bags = [reference_tokens(text, mode) for text in texts]
    output = []
    with localcontext() as context:
        context.prec = 50
        n = Decimal(len(bags))
        mean = Decimal(sum(len(bag) for bag in bags)) / n
        for doc, bag in zip(CORPUS, bags):
            score = Decimal(0)
            for term in set(reference_tokens(query, mode)):
                tf = Decimal(bag.count(term))
                matching_documents = Decimal(len([b for b in bags if term in b]))
                idf = ((n + 1) / (matching_documents + Decimal("0.5"))).ln()
                saturation = tf / (tf + Decimal("1.2") * (Decimal("0.25") + Decimal("0.75") * Decimal(len(bag)) / mean))
                score += idf * Decimal("2.2") * saturation
            output.append({"id": doc["id"], "score": float(score)})
    return sorted(output, key=lambda item: (-item["score"], item["id"]))[:3]


def query_result(query: dict[str, Any], **configuration: Any) -> dict[str, Any]:
    result = retrieve(query["query"], query.get("window", ("2026-01-01", "2026-01-08")), **configuration)
    actual_id = result["definition"]["id"] if result["definition"] else None
    return {"query": query, "result": result, "passed": result["status"] == query["status"] and actual_id == query["id"]}


def calibration(queries: list[dict[str, Any]]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    rows = []
    for mode in ("bigram", "unigram"):
        for threshold in (1.0, 2.0, 4.0, 6.0, 8.0):
            for margin in (0.05, 0.15, 0.3, 0.5):
                configuration = {"mode": mode, "threshold": threshold, "margin": margin}
                correct = sum(query_result(q, **configuration)["passed"] for q in queries if q["split"] == "calibration")
                rows.append({**configuration, "correct": correct})
    # Predeclared conservative tie rule: bigram, higher threshold, higher margin.
    winner = max(rows, key=lambda row: (row["correct"], row["mode"] == "bigram", row["threshold"], row["margin"]))
    return winner, rows


def run(output: Path) -> dict[str, Any]:
    output.mkdir(parents=True, exist_ok=False)
    queries = json.loads((ROOT / "development_queries.json").read_text(encoding="utf-8-sig"))
    winner, grid = calibration(queries)
    locked_matches = all(winner[k] == CONFIG[{"mode": "tokenizer"}.get(k, k)] for k in ("mode", "threshold", "margin"))
    results = [query_result(q) for q in queries]
    reference_checks = []
    for q in queries:
        for mode in ("unigram", "bigram"):
            actual, expected = rank(q["query"], mode), reference_rank(q["query"], mode)
            reference_checks.append({"query": q["query"], "mode": mode, "actual": actual, "reference": expected,
                "passed": all(a["id"] == e["id"] and abs(a["score"] - e["score"]) < 1e-12 for a, e in zip(actual, expected))})
    report = {"environment": {"python": sys.version, "platform": platform.platform()}, "purpose": "development_regression_not_frozen_acceptance",
        "configuration": CONFIG, "selected_calibration": winner, "config_matches_calibration": locked_matches,
        "calibration_grid": grid, "results": results, "reference_checks": reference_checks,
        "hashes": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.iterdir() if p.suffix in (".py", ".json")},
        "passed": locked_matches and all(r["passed"] for r in results + reference_checks)}
    (output / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report
