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


def build_snapshot(root: Path, *, scenario: str, seed: int, base_start: datetime = START,
                   new_version: str = "2.0", crash_probability: float = .65,
                   campaign_channel: str = "paid", campaign_growth: float = 3.0,
                   campaign_retention: float = .12, campaign_unit_cost: int = 200) -> Snapshot:
    if base_start.tzinfo is None or not new_version or new_version == "1.0" or not 0 <= crash_probability <= 1:
        raise ValueError("Invalid development parameters")
    if (not campaign_channel or campaign_channel in ("organic", "idle")
            or not 0 <= campaign_growth <= 10 or not 0 <= campaign_retention <= 1
            or type(campaign_unit_cost) is not int or campaign_unit_cost < 0):
        raise ValueError("Invalid development channel parameters")
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
        date = base_start + timedelta(days=day)
        counts = {"organic": 0, campaign_channel: 0}
        for os in ("Android", "iOS"):
            for channel in ("organic", campaign_channel):
                scale = 1 + (day % 3 - 1) * .1
                volume = 60
                if scenario == "A2" and day >= 7 and channel == campaign_channel:
                    volume = round(60 * campaign_growth)
                if scenario == "A4" and day >= 7:
                    volume = 40 if os == "Android" else 80
                for index in range(round(volume * scale)):
                    uid = f"u{day:02d}-{os}-{channel}-{index:03d}"
                    version = new_version if day >= 7 and os == "Android" and index % 2 == 0 else "1.0"
                    registered = date + timedelta(hours=23, minutes=50) if index == 0 else date + timedelta(hours=8)
                    rows["users"].append((uid, registered, os, version, channel))
                    counts[channel] += 1
                    affected_version = day >= 7 and os == "Android" and version == new_version
                    entity_crash_probability = crash_probability if scenario == "A1" and affected_version else .02
                    crashed = draw(seed, uid, "crash") < entity_crash_probability
                    sid = uid + "-first"
                    rows["sessions"].append((sid, uid, registered + timedelta(minutes=1), os, version, crashed))
                    probability = .5 if os == "Android" else .9
                    if scenario == "A1" and affected_version and crashed:
                        probability = .05
                    if scenario == "A2" and day >= 7 and channel == campaign_channel:
                        probability = campaign_retention
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
            unit_cost = 100 if channel == campaign_channel else 20
            if scenario == "A2" and day >= 7 and channel == campaign_channel:
                unit_cost = campaign_unit_cost
            rows["channel_daily"].append((date.date(), channel, count * unit_cost))
        rows["channel_daily"].append((date.date(), "idle", 100))
    rows["release_calendar"] = [("Android", "1.0", base_start - timedelta(days=30)),
                                 ("iOS", "1.0", base_start - timedelta(days=30)),
                                 ("Android", new_version, base_start + timedelta(days=7))]
    rows["source_watermarks"] = [(name, base_start + timedelta(days=16)) for name in TABLES if name != "source_watermarks"]
    if scenario == "insufficient":
        session_cutoff, telemetry_cutoff = base_start + timedelta(days=11), base_start + timedelta(days=7)
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
        "logical_hash": logical_hash, "human_review": "pending", "mechanism": (f"Android {new_version} first-day crash probability {crash_probability}; crashed users return with probability .05." if scenario == "A1" else f"{campaign_channel} current volume multiplier {campaign_growth}; return probability {campaign_retention}; unit spend {campaign_unit_cost} cents." if scenario == "A2" else MECHANISMS[scenario]),
        "parameters": {"base_start": base_start.date().isoformat(), "current_start": (base_start + timedelta(days=7)).date().isoformat(), "end": (base_start + timedelta(days=14)).date().isoformat(), "new_version": new_version, "crash_probability": crash_probability, "campaign_channel": campaign_channel, "campaign_growth": campaign_growth, "campaign_retention": campaign_retention, "campaign_unit_cost": campaign_unit_cost},
        "purpose": "development_only"}, indent=2), encoding="utf-8")
    return Snapshot(database, manifest, logical_hash)
