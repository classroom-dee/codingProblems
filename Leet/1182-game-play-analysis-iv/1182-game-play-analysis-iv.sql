SELECT ROUND(
    COUNT(DISTINCT a.player_id) /
    (SELECT COUNT(DISTINCT player_id) FROM Activity),
    2
) AS fraction
FROM Activity a
WHERE (a.player_id, a.event_date) IN (
    SELECT
        player_id,
        DATE_ADD(MIN(event_date), INTERVAL 1 DAY) # the next day after the first log ion
    FROM Activity
    GROUP BY player_id
);

