-- SELECT player_id, event_date as first_login
-- FROM
-- (
--     SELECT 
--         player_id, 
--         event_date, 
--         RANK() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS rnk
--     FROM activity
-- ) t
-- WHERE rnk = 1;

SELECT player_id, MIN(event_date) as first_login
FROM activity
GROUP BY player_id;