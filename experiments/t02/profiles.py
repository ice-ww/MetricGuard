"""Immutable source-reviewed schemas; no model/request supplied schema is accepted."""

LEGACY_SCHEMA = {
    "sales": {"id": "INTEGER", "region_id": "INTEGER", "amount": "INTEGER"},
    "regions": {"id": "INTEGER", "name": "VARCHAR"},
}
BUSINESS_SCHEMA = {
    "users": {"user_id": "VARCHAR", "registered_at": "TIMESTAMP WITH TIME ZONE", "registration_os": "VARCHAR", "registration_version": "VARCHAR", "channel": "VARCHAR"},
    "sessions": {"session_id": "VARCHAR", "user_id": "VARCHAR", "started_at": "TIMESTAMP WITH TIME ZONE", "os": "VARCHAR", "version": "VARCHAR", "crashed": "BOOLEAN"},
    "content_events": {"event_id": "VARCHAR", "play_id": "VARCHAR", "session_id": "VARCHAR", "event_type": "VARCHAR", "occurred_at": "TIMESTAMP WITH TIME ZONE"},
    "playback_telemetry": {"report_id": "VARCHAR", "play_id": "VARCHAR", "session_id": "VARCHAR", "observed_at": "TIMESTAMP WITH TIME ZONE", "watched_seconds": "INTEGER", "duration_seconds": "INTEGER"},
    "channel_daily": {"day": "DATE", "channel": "VARCHAR", "spend_cents": "BIGINT"},
    "release_calendar": {"os": "VARCHAR", "version": "VARCHAR", "released_at": "TIMESTAMP WITH TIME ZONE"},
    "source_watermarks": {"source": "VARCHAR", "complete_before": "TIMESTAMP WITH TIME ZONE"},
}
PROFILES = {"legacy": LEGACY_SCHEMA, "business": BUSINESS_SCHEMA}


def identify_profile(tables: list, columns: list) -> str:
    """Match exact physical tables and ordered column names/types, fail closed."""
    for name, schema in PROFILES.items():
        expected_tables = [("main", table, "BASE TABLE") for table in sorted(schema)]
        expected_columns = [("main", table, column, kind) for table in sorted(schema)
                            for column, kind in schema[table].items()]
        if tables == expected_tables and columns == expected_columns:
            return name
    raise ValueError("Snapshot does not match a reviewed physical schema")
