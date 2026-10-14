"""Reviewed business profiles. Still executed through the ordinary SQL sandbox."""
from datetime import date
from collections.abc import Callable


def comparison_window(window: list[str]) -> list[str]:
    start, end = map(date.fromisoformat, window)
    return [(start - (end - start)).isoformat(), window[1]]


def cohort_health(window: list[str], *, previous_start: str | None = None, previous_end: str | None = None) -> str:
    previous, end = comparison_window(window)
    previous = previous_start or previous
    start = window[0]
    previous_end = previous_end or start
    return f"""WITH cohort AS (
        SELECT u.user_id, u.registration_os, u.registration_version,
          CASE WHEN CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE) < '{start}' THEN 'previous' ELSE 'current' END AS period,
          CASE WHEN EXISTS (SELECT 1 FROM sessions s WHERE s.user_id=u.user_id
            AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)+1) THEN 1 ELSE 0 END AS retained,
          CASE WHEN EXISTS (SELECT 1 FROM sessions s WHERE s.user_id=u.user_id AND s.crashed=TRUE
            AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)) THEN 1 ELSE 0 END AS crashed
        FROM users u WHERE ((CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{previous}'
          AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{previous_end}')
          OR (CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{start}'
          AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{end}')))
        SELECT period, registration_os, registration_version, COUNT(*) AS users,
          SUM(retained) AS retained, SUM(crashed) AS crashed_users,
          SUM(retained)*1.0/NULLIF(COUNT(*),0) AS retention_rate,
          SUM(crashed)*1.0/NULLIF(COUNT(*),0) AS crash_rate,
          CASE WHEN period='previous' THEN '{previous}' ELSE '{start}' END AS window_start,
          CASE WHEN period='previous' THEN '{previous_end}' ELSE '{end}' END AS window_end
        FROM cohort GROUP BY period, registration_os, registration_version
        ORDER BY period, registration_os, registration_version"""


def crash_versions(window: list[str], *, previous_start: str | None = None, previous_end: str | None = None) -> str:
    previous, end = comparison_window(window)
    previous = previous_start or previous
    start = window[0]
    previous_end = previous_end or start
    return f"""SELECT CASE WHEN CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{start}'
        THEN 'previous' ELSE 'current' END AS period, u.registration_os, u.registration_version,
        s.os AS actual_os, s.version AS actual_version, COUNT(DISTINCT u.user_id) AS crashed_users,
        CASE WHEN CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{start}' THEN '{previous}' ELSE '{start}' END AS window_start,
        CASE WHEN CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{start}' THEN '{previous_end}' ELSE '{end}' END AS window_end
        FROM users u JOIN sessions s ON s.user_id=u.user_id
        WHERE ((CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{previous}'
        AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{previous_end}')
        OR (CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{start}'
        AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{end}')) AND s.crashed=TRUE
        AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)
        GROUP BY period, u.registration_os, u.registration_version, s.os, s.version, window_start, window_end
        ORDER BY period, u.registration_os, u.registration_version, s.os, s.version"""


def releases(window: list[str]) -> str:
    return f"""SELECT os, version, CAST(released_at AT TIME ZONE 'Asia/Shanghai' AS DATE) AS release_date
        FROM release_calendar WHERE CAST(released_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{window[1]}'
        ORDER BY os, version, release_date"""


def channel_health(window: list[str], *, previous_start: str | None = None, previous_end: str | None = None) -> str:
    previous, end = comparison_window(window)
    previous = previous_start or previous
    start = window[0]
    previous_end = previous_end or start
    return f"""WITH cohort AS (
        SELECT u.channel,
          CASE WHEN CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{start}' THEN 'previous' ELSE 'current' END AS period,
          CASE WHEN EXISTS (SELECT 1 FROM sessions s WHERE s.user_id=u.user_id
            AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)+1) THEN 1 ELSE 0 END AS retained
        FROM users u WHERE ((CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{previous}'
          AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{previous_end}')
          OR (CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{start}'
          AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{end}'))),
        counts AS (SELECT period,channel,COUNT(*) AS users,SUM(retained) AS retained FROM cohort GROUP BY period,channel),
        costs AS (SELECT CASE WHEN day<'{start}' THEN 'previous' ELSE 'current' END AS period,
          channel,SUM(spend_cents) AS spend_cents FROM channel_daily WHERE ((day>='{previous}' AND day<'{previous_end}') OR (day>='{start}' AND day<'{end}')) GROUP BY period,channel),
        base AS (SELECT COALESCE(n.period,k.period) AS period,COALESCE(n.channel,k.channel) AS channel,
          COALESCE(n.users,0) AS users,COALESCE(n.retained,0) AS retained,k.spend_cents
          FROM counts n FULL JOIN costs k ON n.channel=k.channel AND n.period=k.period)
        SELECT period,channel,users,retained,retained*1.0/NULLIF(users,0) AS retention_rate,spend_cents,
          spend_cents*1.0/NULLIF(users,0) AS cost_per_new_cents,
          spend_cents*1.0/NULLIF(retained,0) AS cost_per_retained_cents,
          CASE WHEN period='previous' THEN '{previous}' ELSE '{start}' END AS window_start,
          CASE WHEN period='previous' THEN '{previous_end}' ELSE '{end}' END AS window_end
        FROM base ORDER BY period,channel"""


def system_retention(window: list[str], *, previous_start: str | None = None, previous_end: str | None = None) -> str:
    previous, end = comparison_window(window)
    previous = previous_start or previous
    start = window[0]
    previous_end = previous_end or start
    return f"""WITH cohort AS (
        SELECT u.registration_os,
          CASE WHEN CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{start}' THEN 'previous' ELSE 'current' END AS period,
          CASE WHEN EXISTS (SELECT 1 FROM sessions s WHERE s.user_id=u.user_id
            AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)+1) THEN 1 ELSE 0 END AS retained
        FROM users u WHERE ((CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{previous}'
          AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{previous_end}')
          OR (CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{start}'
          AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{end}')))
        SELECT period,registration_os,COUNT(*) AS users,SUM(retained) AS retained,
          SUM(retained)*1.0/COUNT(*) AS retention_rate,
          CASE WHEN period='previous' THEN '{previous}' ELSE '{start}' END AS window_start,
          CASE WHEN period='previous' THEN '{previous_end}' ELSE '{end}' END AS window_end
        FROM cohort GROUP BY period,registration_os ORDER BY period,registration_os"""


from metricguard.playback_profiles import playback_events, playback_progress
from metricguard.count_profiles import new_user_counts, retained_user_counts, crash_user_counts, channel_spend

COMPARISON_PROFILES = frozenset(('cohort_health', 'crash_versions', 'channel_health', 'system_retention',
    'playback_events', 'playback_progress', 'play_start_counts'))

BUSINESS_PROFILES: dict[tuple[str, str, str], Callable[..., str]] = {('content_events', 'play_id', 'playback_events'): playback_events,
                     ('users','user_id','new_user_counts'):new_user_counts,
                     ('users','user_id','retained_user_counts'):retained_user_counts,
                     ('users','user_id','crash_user_counts'):crash_user_counts,
                     ('content_events','play_id','play_start_counts'):playback_events,
                     ('channel_daily','spend_cents','channel_spend'):channel_spend,
                     ('users', 'registration_os', 'system_retention'): system_retention,
                     ('playback_telemetry', 'play_id', 'playback_progress'): playback_progress,
                     ('users', 'channel', 'channel_health'): channel_health,
                     ('users', 'registration_version', 'cohort_health'): cohort_health,
                     ('sessions', 'version', 'crash_versions'): crash_versions,
                     ('release_calendar', 'version', 'releases'): releases}


def is_business_profile(action: dict) -> bool:
    return action.get('action') == 'profile' and (action.get('table'), action.get('column'), action.get('kind')) in BUSINESS_PROFILES
