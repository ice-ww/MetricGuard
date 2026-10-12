WITH starts AS (
    SELECT play_id, session_id, min(occurred_at) AS began
    FROM content_events WHERE event_type='start' GROUP BY play_id, session_id
), completed AS (
    SELECT DISTINCT play_id, session_id FROM content_events WHERE event_type='complete'
), telemetry AS (
    SELECT play_id, session_id, max(watched_seconds) AS watched, max(duration_seconds) AS duration
    FROM playback_telemetry GROUP BY play_id, session_id
)
SELECT s.os, s.version, count(*) AS starts,
       count(c.play_id) AS completions,
       count(*) FILTER(WHERE t.watched>=t.duration) AS telemetry_complete,
       count(*) FILTER(WHERE t.watched>=t.duration AND c.play_id IS NULL) AS missing_complete,
       count(*) FILTER(WHERE t.play_id IS NULL) AS unmatched,
       count(*) FILTER(WHERE t.watched>=least(5,t.duration)) AS effective,
       coalesce(sum(t.watched),0)::BIGINT AS watched_seconds
FROM starts p JOIN sessions s USING(session_id)
LEFT JOIN completed c ON p.play_id=c.play_id AND p.session_id=c.session_id
LEFT JOIN telemetry t ON p.play_id=t.play_id AND p.session_id=t.session_id
WHERE CAST(p.began AT TIME ZONE 'Asia/Shanghai' AS DATE)>=CAST($start AS DATE)
  AND CAST(p.began AT TIME ZONE 'Asia/Shanghai' AS DATE)<CAST($end AS DATE)
GROUP BY s.os,s.version ORDER BY s.os,s.version
