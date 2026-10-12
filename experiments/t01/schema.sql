CREATE TABLE users(user_id VARCHAR PRIMARY KEY, registered_at TIMESTAMPTZ,
    registration_os VARCHAR, registration_version VARCHAR, channel VARCHAR);
CREATE TABLE sessions(session_id VARCHAR PRIMARY KEY, user_id VARCHAR,
    started_at TIMESTAMPTZ, os VARCHAR, version VARCHAR, crashed BOOLEAN);
CREATE TABLE content_events(event_id VARCHAR PRIMARY KEY, play_id VARCHAR,
    session_id VARCHAR, event_type VARCHAR, occurred_at TIMESTAMPTZ);
CREATE TABLE playback_telemetry(report_id VARCHAR PRIMARY KEY, play_id VARCHAR,
    session_id VARCHAR, observed_at TIMESTAMPTZ, watched_seconds INTEGER,
    duration_seconds INTEGER);
CREATE TABLE channel_daily(day DATE, channel VARCHAR, spend_cents BIGINT,
    PRIMARY KEY(day, channel));
CREATE TABLE release_calendar(os VARCHAR, version VARCHAR, released_at TIMESTAMPTZ);
CREATE TABLE source_watermarks(source VARCHAR PRIMARY KEY, complete_before TIMESTAMPTZ);
