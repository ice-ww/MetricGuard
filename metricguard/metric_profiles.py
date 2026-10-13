"""Reviewed business profiles. Still executed through the ordinary SQL sandbox."""
from datetime import date


def comparison_window(window: list[str]) -> list[str]:
    start, end = map(date.fromisoformat, window)
    return [(start - (end - start)).isoformat(), window[1]]


def cohort_health(window: list[str]) -> str:
    previous, end = comparison_window(window)
    start = window[0]
    return f"""WITH cohort AS (
        SELECT u.user_id, u.registration_os, u.registration_version,
          CASE WHEN CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE) < '{start}' THEN 'previous' ELSE 'current' END AS period,
          CASE WHEN EXISTS (SELECT 1 FROM sessions s WHERE s.user_id=u.user_id
            AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)+1) THEN 1 ELSE 0 END AS retained,
          CASE WHEN EXISTS (SELECT 1 FROM sessions s WHERE s.user_id=u.user_id AND s.crashed=TRUE
            AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)) THEN 1 ELSE 0 END AS crashed
        FROM users u WHERE CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{previous}'
          AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{end}')
        SELECT period, registration_os, registration_version, COUNT(*) AS users,
          SUM(retained) AS retained, SUM(crashed) AS crashed_users,
          SUM(retained)*1.0/NULLIF(COUNT(*),0) AS retention_rate,
          SUM(crashed)*1.0/NULLIF(COUNT(*),0) AS crash_rate,
          CASE WHEN period='previous' THEN '{previous}' ELSE '{start}' END AS window_start,
          CASE WHEN period='previous' THEN '{start}' ELSE '{end}' END AS window_end
        FROM cohort GROUP BY period, registration_os, registration_version
        ORDER BY period, registration_os, registration_version"""


def crash_versions(window: list[str]) -> str:
    previous, end = comparison_window(window)
    start = window[0]
    return f"""SELECT CASE WHEN CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{start}'
        THEN 'previous' ELSE 'current' END AS period, u.registration_os, u.registration_version,
        s.os AS actual_os, s.version AS actual_version, COUNT(DISTINCT u.user_id) AS crashed_users,
        CASE WHEN CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{start}' THEN '{previous}' ELSE '{start}' END AS window_start,
        CASE WHEN CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{start}' THEN '{start}' ELSE '{end}' END AS window_end
        FROM users u JOIN sessions s ON s.user_id=u.user_id
        WHERE CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{previous}'
        AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{end}' AND s.crashed=TRUE
        AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)
        GROUP BY period, u.registration_os, u.registration_version, s.os, s.version, window_start, window_end
        ORDER BY period, u.registration_os, u.registration_version, s.os, s.version"""


def releases(window: list[str]) -> str:
    return f"""SELECT os, version, CAST(released_at AT TIME ZONE 'Asia/Shanghai' AS DATE) AS release_date
        FROM release_calendar WHERE CAST(released_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{window[1]}'
        ORDER BY os, version, release_date"""


BUSINESS_PROFILES = {('users', 'registration_version', 'cohort_health'): cohort_health,
                     ('sessions', 'version', 'crash_versions'): crash_versions,
                     ('release_calendar', 'version', 'releases'): releases}


def is_business_profile(action: dict) -> bool:
    return action.get('action') == 'profile' and (action.get('table'), action.get('column'), action.get('kind')) in BUSINESS_PROFILES
