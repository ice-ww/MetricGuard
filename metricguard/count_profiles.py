"""Reviewed standalone counts; each query keeps its own source/window contract."""


def new_user_counts(window: list[str]) -> str:
    return f"""SELECT COUNT(DISTINCT user_id) AS users FROM users
        WHERE CAST(registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{window[0]}'
        AND CAST(registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{window[1]}'"""


def retained_user_counts(window: list[str]) -> str:
    return f"""WITH cohort AS (SELECT u.user_id,u.registration_os,
        CASE WHEN EXISTS (SELECT 1 FROM sessions s WHERE s.user_id=u.user_id
        AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)+1)
        THEN 1 ELSE 0 END AS retained FROM users u
        WHERE CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{window[0]}'
        AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{window[1]}')
        SELECT registration_os,COUNT(*) AS users,SUM(retained) AS retained,SUM(retained)*1.0/NULLIF(COUNT(*),0) AS retention_rate
        FROM cohort GROUP BY registration_os ORDER BY registration_os"""


def crash_user_counts(window: list[str]) -> str:
    return f"""SELECT COUNT(*) AS users,SUM(CASE WHEN EXISTS (
        SELECT 1 FROM sessions s WHERE s.user_id=u.user_id AND s.crashed=TRUE
        AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE)=CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE))
        THEN 1 ELSE 0 END) AS crashed_users FROM users u
        WHERE CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)>='{window[0]}'
        AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)<'{window[1]}'"""


def channel_spend(window: list[str]) -> str:
    return f"""SELECT channel,SUM(spend_cents) AS spend_cents FROM channel_daily
        WHERE day>='{window[0]}' AND day<'{window[1]}' GROUP BY channel ORDER BY channel"""


COUNT_PROMPT = '''For standalone queries without anomaly diagnosis, trusted count profiles are available:
users, user_id, new_user_counts: current-window total newly registered users.
users, user_id, retained_user_counts: current-window mature new users, D1 retained users and retention rate by system; trusted report computes pooled totals.
users, user_id, crash_user_counts: current-window newly registered users and first-day crash-affected users.
content_events, play_id, play_start_counts: deduplicated starts by actual system/version, with both periods.
channel_daily, spend_cents, channel_spend: current-window spend in cents by channel.
Return normal profile actions using these (table,column,kind) tuples. Count profiles return all relevant groups;
cite the requested group in the report, never guess group counts. They do not establish anomaly explanations.
For iterative diagnosis, stop after a successful standalone count profile only if it answers a simple count/rate query.
Anomaly assessment, change explanations and evidence-sufficiency questions require BOTH current and previous periods.
For general retention anomaly or completeness assessment use system_retention; standalone retained_user_counts cannot answer it.
Comparison profiles preserve the preceding requested-length comparison period even when source completeness shortens the current period.
A shortened current period cannot establish a conclusion for the entire requested window; disclose insufficiency.
'''
