from __future__ import annotations
import json
import math
import re
import unicodedata
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent
CORPUS = json.loads((ROOT / "corpus.json").read_text(encoding="utf-8-sig"))
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8-sig"))

def tokenize(text: str, mode: str = "bigram") -> list[str]:
    text = unicodedata.normalize("NFKC", text).lower()
    out: list[str] = []
    for run in re.findall(r"[\u4e00-\u9fff]+|[a-z0-9_]+", text):
        if re.fullmatch(r"[\u4e00-\u9fff]+", run):
            out.extend(list(run) if mode == "unigram" else [run[i:i+2] for i in range(len(run)-1)])
        else:
            out.append(run)
    return out

def normalize(text: str) -> str:
    return re.sub(r"\s+", "", unicodedata.normalize("NFKC", text).lower())

def rank(query: str, mode: str | None = None) -> list[dict[str, Any]]:
    mode = mode or CONFIG["tokenizer"]
    docs = [tokenize(" ".join([d["name"], *d["aliases"], d["definition"]]), mode) for d in CORPUS]
    avg = sum(map(len, docs)) / len(docs)
    scores = []
    for definition, document in zip(CORPUS, docs):
        counts = Counter(document)
        score = 0.0
        for term in sorted(set(tokenize(query, mode))):
            frequency = counts[term]
            df = sum(term in doc for doc in docs)
            idf = math.log(1 + (len(docs) - df + 0.5) / (df + 0.5))
            score += idf * frequency * 2.2 / (frequency + 1.2 * (0.25 + 0.75 * len(document)/avg))
        scores.append({"id": definition["id"], "score": score})
    return sorted(scores, key=lambda d: (-d["score"], d["id"]))[:3]

def retrieve(query: str, window: tuple[str, str] | None = None,
             threshold: float | None = None, margin: float | None = None,
             mode: str | None = None) -> dict[str, Any]:
    threshold = CONFIG["threshold"] if threshold is None else threshold
    margin = CONFIG["margin"] if margin is None else margin
    candidates = rank(query, mode)
    exact = [d for d in CORPUS if normalize(query) in [normalize(d["name"]), *map(normalize, d["aliases"])]]
    chosen = exact[0] if len(exact) == 1 else None
    method = "exact" if chosen else "bm25"
    reason = "matched"
    status = "adopt"
    normalized = normalize(query)
    if chosen is None:
        named=[d for d in CORPUS if any(normalize(name) in normalized for name in [d['name'],*d['aliases']])]
        if len(named)==1:
            chosen,method=named[0],'named'
        elif len(named)>1:
            status,reason='clarify','candidate_ambiguity'
    # Component metrics have their own denominators and source completeness;
    # do not silently reinterpret a requested count as its associated rate.
    from experiments.t06.components import component_definition
    component = component_definition(normalized)
    if component is not None:
        chosen, method = component, 'named_component'
    elif all(term in normalized for term in ('新增', '留存', '渠道', '成本')) and not any(term in normalized for term in ('次日','第二天')):
        chosen = next(d for d in CORPUS if d['id'] == 'retained_cost')
        method = 'named_components'
    elif '用户表现' in normalized and not any(term in normalized for term in ('留存', '完播', '有效播放', '成本', '崩溃')):
        status, reason = 'clarify', 'metric_required'
    if "留存" in normalized and (any(term in normalized for term in ("小时", "七日", "月留存", "老用户", "活跃用户")) or re.search(r"\d+日", normalized)):
        status, reason = "unsupported", "unsupported_population_or_horizon"
    elif "留存" in normalized and not any(term in normalized for term in ("新增", "新用户", "注册", "成本", "获客")):
        status, reason = "clarify", "retention_population_required"
    elif "留存" in normalized and not any(term in normalized for term in ("次日", "第二天", "成本", "获客")):
        status, reason = "clarify", "retention_horizon_required"
    if chosen is None and status == "adopt":
        if candidates[0]["score"] < threshold:
            status, reason = "unsupported", "no_supported_definition"
        elif (candidates[0]["score"] - candidates[1]["score"]) / candidates[0]["score"] < margin:
            status, reason = "clarify", "candidate_ambiguity"
        else:
            chosen = next(d for d in CORPUS if d["id"] == candidates[0]["id"])
    if status == "adopt" and window is None:
        status, reason = "clarify", "time_window_required"
    elif status == "adopt" and window is not None:
        try:
            if len(window) != 2 or date.fromisoformat(window[0]) >= date.fromisoformat(window[1]):
                raise ValueError("empty interval")
        except (ValueError, TypeError, IndexError):
            status, reason = "clarify", "invalid_time_window"
    return {"status": status, "reason": reason, "method": method,
            "definition": chosen if status == "adopt" else None,
            "candidates": candidates, "window": window, "corpus_version": "t06-v1"}
