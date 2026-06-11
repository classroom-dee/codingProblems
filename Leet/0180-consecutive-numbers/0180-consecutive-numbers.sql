SELECT DISTINCT l.num AS ConsecutiveNums
FROM
(
    SELECT
        id,
        num,
        LAG(num) OVER (ORDER BY id ASC) AS prev_num,
        LAG(num, 2) OVER (ORDER BY id ASC) AS prev_prev_num
    FROM Logs
) l
WHERE l.prev_num = l.num AND l.prev_prev_num = l.num

-- -- Readability version
-- WITH numbered AS (
--     SELECT
--         id,
--         num,
--         LAG(num) OVER (ORDER BY id) AS prev_num,
--         LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
--     FROM Logs
-- )
-- SELECT DISTINCT num AS ConsecutiveNums
-- FROM numbered
-- WHERE num = prev_num AND num = prev_prev_num