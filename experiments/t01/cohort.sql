SELECT u.user_id, u.registration_os AS os, u.registration_version AS version, u.channel,
       EXISTS(SELECT 1 FROM sessions s WHERE s.user_id=u.user_id
           AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE) =
               CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)+1) AS retained,
       EXISTS(SELECT 1 FROM sessions s WHERE s.user_id=u.user_id AND s.crashed
           AND CAST(s.started_at AT TIME ZONE 'Asia/Shanghai' AS DATE) =
               CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE)) AS crashed
FROM users u
WHERE CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE) >= CAST($start AS DATE)
  AND CAST(u.registered_at AT TIME ZONE 'Asia/Shanghai' AS DATE) < CAST($end AS DATE)
