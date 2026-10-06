-- SELECT 
--     id,
--     (
--         CASE 
--             WHEN id - lag(id) OVER (ORDER BY id) = 1 THEN 1
--             ELSE NULL
--         END
--     ) AS lagged
-- FROM stadium
-- WHERE people >= 100

WITH s AS (
    SELECT
        id, 
        visit_date,
        people,
        (id - ROW_NUMBER() OVER (ORDER BY id)) AS rn
    FROM stadium
    WHERE people >= 100
), ss AS (
SELECT id, visit_date, people, COUNT(*) OVER (PARTITION BY rn) AS cnt
FROM s
)
SELECT id, visit_date, people
FROM ss
WHERE cnt > 2
ORDER BY visit_date ASC