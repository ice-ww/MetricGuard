"""Bounded worker result materialization; supervisor also bounds wire bytes."""

import json
import time
from typing import Any

import duckdb

MAX_ROWS = 1000
MAX_COLUMNS = 64
MAX_CELL_BYTES = 64 * 1024
MAX_RESULT_BYTES = 1024 * 1024
# Leave space for trusted settings, timings and envelope on the wire.
ROW_BYTES = MAX_RESULT_BYTES - 16 * 1024


def bounded_result(cursor: duckdb.DuckDBPyConnection) -> dict[str, Any]:
    fetch_seconds = serialize_seconds = 0.0
    rows: list[list[Any]] = []
    byte_count = 2
    result: dict[str, Any] = {"status": "ok", "rows": rows, "truncated": False}
    if len(cursor.description or ()) > MAX_COLUMNS:
        return {"status": "output_limit", "limit": "columns", "fetch_seconds": 0.0, "serialize_seconds": 0.0}
    columns = [{"name": item[0], "type": str(item[1])} for item in (cursor.description or ())]
    metadata_bytes = len(json.dumps(columns, ensure_ascii=True).encode("utf-8"))
    if metadata_bytes > 8192:
        return {"status": "output_limit", "limit": "column_metadata", "fetch_seconds": 0.0, "serialize_seconds": 0.0}
    if len({item["name"].casefold() for item in columns}) != len(columns):
        return {"status": "output_limit", "limit": "duplicate_columns", "fetch_seconds": 0.0, "serialize_seconds": 0.0}
    result["columns"] = columns
    for index in range(MAX_ROWS + 1):
        tick = time.monotonic()
        row = cursor.fetchone()
        fetch_seconds += time.monotonic() - tick
        if row is None:
            break
        if index == MAX_ROWS:
            result["truncated"] = True
            break
        tick = time.monotonic()
        converted = []
        for cell in row:
            # Complex DuckDB values are not part of the approved scalar result
            # contract. Never recursively materialize them into JSON.
            if isinstance(cell, (list, tuple, dict, bytes, bytearray)):
                result = {"status": "output_limit", "limit": "unsupported_cell"}
                break
            value = cell if cell is None or isinstance(cell, (str, int, float, bool)) else str(cell)
            if isinstance(value, str) and len(value) > MAX_CELL_BYTES:
                result = {"status": "output_limit", "limit": "cell_bytes"}
                break
            encoded = json.dumps(value, ensure_ascii=True, default=str)
            if len(encoded.encode("utf-8")) > MAX_CELL_BYTES:
                result = {"status": "output_limit", "limit": "cell_bytes"}
                break
            converted.append(value)
        if result["status"] == "ok":
            encoded_row = json.dumps(converted, ensure_ascii=True, separators=(",", ":"))
            byte_count += len(encoded_row.encode("utf-8")) + bool(rows)
            if byte_count > ROW_BYTES:
                result = {"status": "output_limit", "limit": "result_bytes"}
            else:
                rows.append(converted)
        serialize_seconds += time.monotonic() - tick
        if result["status"] != "ok":
            break
    return {**result, "fetch_seconds": fetch_seconds, "serialize_seconds": serialize_seconds}
