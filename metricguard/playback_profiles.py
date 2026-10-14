"""Bounded aggregate playback profiles; all SQL uses the unchanged sandbox."""
from datetime import date, timedelta

def comparison_window(window: list[str]) -> list[str]:
    start, end = map(date.fromisoformat, window)
    return [(start - (end-start)).isoformat(), window[1]]


def event_base() -> str:
    return """SELECT play_id, MIN(session_id) AS sid, COUNT(DISTINCT session_id) AS sessions,
      MIN(CASE WHEN event_type='start' THEN occurred_at END) AS began,
      MIN(occurred_at) AS first_event,MAX(occurred_at) AS last_event,
      COUNT(DISTINCT CASE WHEN event_type='start' THEN occurred_at END) AS start_times,
      MAX(CASE WHEN event_type='complete' THEN 1 ELSE 0 END) AS completed,
      SUM(CASE WHEN session_id IS NULL OR play_id IS NULL OR occurred_at IS NULL THEN 1 ELSE 0 END) AS invalid
      FROM content_events GROUP BY play_id"""


def grouping(window: list[str], began: str, previous_start: str | None = None, previous_end: str | None = None) -> tuple[str, str]:
    previous, end = comparison_window(window)
    previous = previous_start or previous
    previous_end = previous_end or window[0]
    previous_last = (date.fromisoformat(previous_end) - timedelta(days=1)).isoformat()
    current_last = (date.fromisoformat(end) - timedelta(days=1)).isoformat()
    day = f"CAST({began} AT TIME ZONE 'Asia/Shanghai' AS DATE)"
    return (f"CASE WHEN {day}<'{window[0]}' THEN 'previous' ELSE 'current' END",
            f"({day} BETWEEN '{previous}' AND '{previous_last}' OR {day} BETWEEN '{window[0]}' AND '{current_last}')")


def playback_events(window: list[str], *, previous_start: str | None = None, previous_end: str | None = None) -> str:
    period, where = grouping(window, 'COALESCE(e.began,e.first_event)', previous_start, previous_end)
    return f"""WITH e AS ({event_base()})
      SELECT {period} AS period,s.os AS actual_os,s.version AS actual_version,
      MAX(e.last_event) AS last_event,
      SUM(CASE WHEN e.began IS NOT NULL THEN 1 ELSE 0 END) AS starts,
      SUM(CASE WHEN e.began IS NOT NULL THEN e.completed ELSE 0 END) AS observed_completed,
      SUM(CASE WHEN e.began IS NULL OR e.sessions<>1 OR e.invalid>0 OR e.start_times<>1 OR e.first_event<e.began OR s.session_id IS NULL OR s.os IS NULL OR s.version IS NULL OR s.started_at IS NULL OR s.started_at>e.began THEN 1 ELSE 0 END) AS invalid_alignment
      FROM e LEFT JOIN sessions s ON e.sid=s.session_id WHERE {where}
      GROUP BY period,s.os,s.version ORDER BY period,s.os,s.version"""


def playback_progress(window: list[str], *, previous_start: str | None = None, previous_end: str | None = None) -> str:
    base = """SELECT play_id,MIN(session_id) AS sid,COUNT(DISTINCT session_id) AS sessions,
      MIN(CASE WHEN event_type='start' THEN occurred_at END) AS began,
      MAX(CASE WHEN event_type='complete' THEN 1 ELSE 0 END) AS completed FROM content_events GROUP BY play_id"""
    period, where = grouping(window, 'COALESCE(e.began,t.observed)', previous_start, previous_end)
    return f"""WITH e AS ({base}),
      t AS (SELECT play_id,MIN(session_id) AS sid,COUNT(DISTINCT session_id) AS sessions,
        MIN(observed_at) AS observed, MAX(observed_at) AS last_observed, MAX(watched_seconds) AS watched,
        MIN(duration_seconds) AS duration,MAX(duration_seconds) AS max_duration,
        SUM(CASE WHEN session_id IS NULL OR play_id IS NULL OR observed_at IS NULL OR watched_seconds IS NULL OR duration_seconds IS NULL OR watched_seconds<0 OR duration_seconds<=0 THEN 1 ELSE 0 END) AS invalid
        FROM playback_telemetry GROUP BY play_id),
      p AS (SELECT {period} AS period,s.os AS actual_os,s.version AS actual_version,
        e.completed,t.duration,t.last_observed,
        CASE WHEN e.sessions=1 AND s.started_at<=e.began AND t.sid=e.sid AND t.sessions=1 AND t.invalid=0 AND t.duration=t.max_duration AND t.observed>=e.began AND t.watched<=t.duration THEN t.watched END AS valid_watched,
        CASE WHEN e.began IS NULL OR t.sid<>e.sid OR t.sessions<>1 OR t.play_id IS NULL THEN 1 ELSE 0 END AS unmatched,
        CASE WHEN t.invalid>0 OR t.duration<>t.max_duration OR t.observed<e.began OR t.watched>t.duration THEN 1 ELSE 0 END AS invalid
        FROM e FULL JOIN t ON e.play_id=t.play_id LEFT JOIN sessions s ON e.sid=s.session_id WHERE {where})
      SELECT period,actual_os,actual_version,MAX(last_observed) AS last_observed,
        SUM(unmatched) AS unmatched,SUM(invalid) AS invalid_telemetry,
        SUM(CASE WHEN valid_watched>=duration THEN 1 ELSE 0 END) AS independent_complete,
        SUM(CASE WHEN valid_watched>=duration AND completed=0 THEN 1 ELSE 0 END) AS independent_complete_without_event,
        SUM(CASE WHEN valid_watched>=CASE WHEN duration<5 THEN duration ELSE 5 END THEN 1 ELSE 0 END) AS effective
      FROM p GROUP BY period,actual_os,actual_version"""
