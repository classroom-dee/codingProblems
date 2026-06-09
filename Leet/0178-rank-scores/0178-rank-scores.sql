-- "How many different scores are higher than this score?"

-- 100 â higher scores: none â rank 1

-- 90 â higher distinct scores: 100 â rank 2

-- 90 â higher distinct scores: 100 â rank 2

-- 80 â higher distinct scores: 100, 90 â rank 3

SELECT
    score,
    DENSE_RANK() OVER(ORDER BY score DESC) AS 'rank'
FROM scores

-- Without dense_rank but more expensive:
-- SELECT
--     score,
--     (
--         SELECT COUNT(DISTINCT s1.score) + 1
--         FROM scores s1
--         WHERE s1.score > s2.score
--     ) as 'rank'
-- FROM scores s2
-- ORDER BY score DESC
