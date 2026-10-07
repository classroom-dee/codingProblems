WITH r
AS (
    SELECT r1.requester_id AS id
    FROM requestAccepted r1
    UNION ALL -- union dedupes
    SELECT r2.accepter_id AS id
    FROM requestAccepted r2
)
SELECT 
    id, 
    count(*) AS num
FROM r
GROUP BY id
ORDER BY num DESC
LIMIT 1