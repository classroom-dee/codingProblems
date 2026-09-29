-- SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
-- FROM insurance
-- WHERE tiv_2015 
-- IN (
--     SELECT tiv_2015
--     FROM insurance
--     GROUP BY tiv_2015
--     HAVING COUNT(pid) > 1
-- )
-- AND (lat, lon) 
-- IN (
--     SELECT lat, lon
--     FROM insurance
--     GROUP BY lat, lon
--     HAVING COUNT(pid) < 2
-- )

-- But if (lat,lon) and tiv_2015 had indexes, this could be better
-- or it's just better because it exits early on match
SELECT ROUND(SUM(i1.tiv_2016), 2) AS tiv_2016
FROM insurance i1
WHERE EXISTS
(
    SELECT 1
    FROM insurance i2
    WHERE i1.tiv_2015 = i2.tiv_2015
    AND i1.pid <> i2.pid
)
AND NOT EXISTS
(
    SELECT 1
    FROM insurance i3
    WHERE i1.lat = i3.lat
    AND i1.lon = i3.lon
    AND i1.pid <> i3.pid
)