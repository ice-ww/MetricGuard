"""Deterministic business snapshots; scenario metadata lives outside public data."""

import hashlib
import csv
import json
import random
import tempfile
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import duckdb

SHANGHAI = timezone(timedelta(hours=8))  # Fixed 2026 fixture dates, no DST.
START = datetime(2026, 1, 1, tzinfo=SHANGHAI)
TABLES = ("users", "sessions", "content_events", "playback_telemetry",
          "channel_daily", "release_calendar", "source_watermarks")
MECHANISMS = {
    "normal": "No injected anomaly; seeded Bernoulli activity and daily volume variation.",
    "A1": "Android 2.0 first-day crash probability .65; crashed users return with probability .05.",
    "A2": "Paid campaign triples current acquisition volume; return probability .12; unit spend 200 cents.",
    "A3": "Android 2.0 completion collector drops completions; independent progress remains unchanged.",
    "A4": "Android return probability .30; system mix shifts from 1:1 to 1:2, masking deterioration.",
    "insufficient": "Incomplete export: sessions complete before Jan12; telemetry before Jan08.",
}


@dataclass(frozen=True)
class Snapshot:
    database: Path
    private_manifest: Path
    logical_hash: str
    tables: tuple[str, ...] = TABLES


def draw(seed: int, *key: object) -> float:
    """Stable per-entity streams keep unaffected cohorts identical across scenarios."""
    digest = hashlib.sha256(json.dumps([seed, *key]).encode()).digest()
    return random.Random(int.from_bytes(digest, "big")).random()


def build_snapshot(root: Path, *, scenario: str, seed: int) -> Snapshot:
    if scenario not in MECHANISMS:
        raise ValueError(f"Unknown development scenario: {scenario}")
    if root.exists():
        raise FileExistsError(f"Use a fresh output directory: {root}")
    public = root / "public"
    private = root / "private"
    public.mkdir(parents=True)
    private.mkdir()
    rows: dict[str, list[tuple[Any, ...]]] = {table: [] for table in TABLES}
    for day in range(16):
        date = START + timedelta(days=day)
        counts = {"organic": 0, "paid": 0}
        for os in ("Android", "iOS"):
            for channel in ("organic", "paid"):
                scale = 1 + (day % 3 - 1) * .1
                volume = 60
                if scenario == "A2" and day >= 7 and channel == "paid":
                    volume = 180
                if scenario == "A4" and day >= 7:
                    volume = 40 if os == "Android" else 80
                for index in range(round(volume * scale)):
                    uid = f"u{day:02d}-{os}-{channel}-{index:03d}"
                    version = "2.0" if day >= 7 and os == "Android" and index % 2 == 0 else "1.0"
                    registered = date + timedelta(hours=23, minutes=50) if index == 0 else date + timedelta(hours=8)
                    rows["users"].append((uid, registered, os, version, channel))
                    counts[channel] += 1
                    affected_version = day >= 7 and os == "Android" and version == "2.0"
                    crash_probability = .65 if scenario == "A1" and affected_version else .02
                    crashed = draw(seed, uid, "crash") < crash_probability
                    sid = uid + "-first"
                    rows["sessions"].append((sid, uid, registered + timedelta(minutes=1), os, version, crashed))
                    probability = .5 if os == "Android" else .9
                    if scenario == "A1" and affected_version and crashed:
                        probability = .05
                    if scenario == "A2" and day >= 7 and channel == "paid":
                        probability = .12
                    if scenario == "A4" and day >= 7 and os == "Android":
                        probability = .3
                    if draw(seed, uid, "retention") < probability:
                        # Duplicate next-day sessions must not double-count retained users.
                        for repeat in range(2):
                            rows["sessions"].append((uid + f"-return{repeat}", uid,
                                date + timedelta(days=1, minutes=5 + repeat), os, version, False))
                    for play in range(2):
                        pid = uid + f"-p{play}"
                        at = registered + timedelta(minutes=2 + play)
                        complete = draw(seed, uid, play, "complete") < .75
                        rows["content_events"].append((pid + "-start", pid, sid, "start", at))
                        if complete and not (scenario == "A3" and affected_version):
                            rows["content_events"].append((pid + "-end", pid, sid, "complete", at + timedelta(seconds=30)))
                        rows["playback_telemetry"].append((pid + "-t", pid, sid, at + timedelta(seconds=30), 30 if complete else 3, 30))
                        if index % 10 == 0:
                            rows["content_events"].append((pid + "-dup", pid, sid, "start", at))
                            rows["playback_telemetry"].append((pid + "-td", pid, sid, at + timedelta(seconds=31), 30 if complete else 3, 30))
        for channel, count in counts.items():
            unit_cost = 100 if channel == "paid" else 20
            if scenario == "A2" and day >= 7 and channel == "paid":
                unit_cost = 200
            rows["channel_daily"].append((date.date(), channel, count * unit_cost))
        rows["channel_daily"].append((date.date(), "idle", 100))
    rows["release_calendar"] = [("Android", "1.0", START - timedelta(days=30)),
                                 ("iOS", "1.0", START - timedelta(days=30)),
                                 ("Android", "2.0", START + timedelta(days=7))]
    rows["source_watermarks"] = [(name, START + timedelta(days=16)) for name in TABLES if name != "source_watermarks"]
    if scenario == "insufficient":
        session_cutoff, telemetry_cutoff = START + timedelta(days=11), START + timedelta(days=7)
        rows["sessions"] = [row for row in rows["sessions"] if row[2] < session_cutoff]
        session_ids = {row[0] for row in rows["sessions"]}
        rows["content_events"] = [row for row in rows["content_events"] if row[2] in session_ids]
        rows["playback_telemetry"] = [row for row in rows["playback_telemetry"] if row[3] < telemetry_cutoff]
        rows["source_watermarks"] = [(name, session_cutoff if name in ("sessions", "content_events") else
                                     telemetry_cutoff if name == "playback_telemetry" else cutoff)
                                    for name, cutoff in rows["source_watermarks"]]
    database = public / "snapshot.duckdb"
    with duckdb.connect(str(database)) as con:
        con.execute("BEGIN TRANSACTION")
        con.execute(Path(__file__).with_name("schema.sql").read_text())
        with tempfile.TemporaryDirectory(dir=private) as staging:
            for table, values in rows.items():
                if values:
                    source = Path(staging) / f"{table}.csv"
                    with source.open("w", newline="", encoding="utf-8") as stream:
                        csv.writer(stream).writerows(values)
                    con.execute(f"COPY {table} FROM ? (FORMAT CSV, HEADER FALSE)", [str(source)])
        con.execute("COMMIT")
    logical_hash = hashlib.sha256(json.dumps(rows, default=str, sort_keys=True).encode()).hexdigest()
    manifest = private / "manifest.json"
    manifest.write_text(json.dumps({"scenario": scenario, "seed": seed,
        "logical_hash": logical_hash, "human_review": "pending", "mechanism": MECHANISMS[scenario],
        "parameters": {"base_start": "2026-01-01", "current_start": "2026-01-08", "end": "2026-01-15"},
        "purpose": "development_only"}, indent=2), encoding="utf-8")
    return Snapshot(database, manifest, logical_hash)
