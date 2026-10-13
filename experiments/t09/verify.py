"""Independently verify saved real-model retention results without another API call."""
import argparse
from datetime import date, timedelta, timezone
import hashlib
import json
from pathlib import Path

import duckdb


def verify(database: Path, result_path: Path) -> dict:
    result = json.loads(result_path.read_text(encoding="utf-8"))
    start, end = map(date.fromisoformat, result["actual_window"])
    local = timezone(timedelta(hours=8))
    with duckdb.connect(str(database), read_only=True) as con:
        users = con.execute("SELECT user_id, registered_at FROM users").fetchall()
        sessions = con.execute("SELECT user_id, started_at FROM sessions").fetchall()
    active = {(uid, instant.astimezone(local).date()) for uid, instant in sessions}
    cohorts: dict[date, set[str]] = {}
    for uid, instant in users:
        day = instant.astimezone(local).date()
        if start <= day < end:
            cohorts.setdefault(day, set()).add(uid)
    expected = []
    for day, members in sorted(cohorts.items()):
        retained = sum((uid, day + timedelta(days=1)) in active for uid in members)
        expected.append({"reg_date": day.isoformat(), "new_users": len(members),
                         "retained_users": retained, "retention_rate": retained / len(members)})
    evidence = result["evidence"][0]
    assert evidence["rows"] == expected, "daily independent sets disagree"
    facts = result["report"]["facts"]
    expected_positions = {(row, column) for row in range(len(expected))
                          for column in ("new_users", "retained_users", "retention_rate")}
    assert {(fact["row"], fact["column"]) for fact in facts} == expected_positions
    for fact in facts:
        assert fact["value"] == expected[fact["row"]][fact["column"]]
        assert fact["context"]["group"] == {"reg_date": expected[fact["row"]]["reg_date"]}
    assert result["query_result"]["cleanup_verified"]
    model_attempts = [a for a in result["attempts"] if a["kind"] == "model"]
    assert sum(a["actual"] for a in model_attempts) == result["tokens"]
    return {"passed": True, "method": "raw SELECT then Python timezone/set membership; no model SQL aggregation",
            "database_sha256": hashlib.sha256(database.read_bytes()).hexdigest(),
            "task_id": result["id"], "daily_expected": expected,
            "facts_checked": len(facts), "known_tokens": result["tokens"],
            "total_users": sum(r["new_users"] for r in expected),
            "total_retained": sum(r["retained_users"] for r in expected)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("database", type=Path)
    parser.add_argument("result", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    checked = verify(args.database, args.result)
    args.output.write_text(json.dumps(checked, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(checked))
