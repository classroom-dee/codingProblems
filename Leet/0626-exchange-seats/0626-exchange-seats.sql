SELECT
    CASE
        WHEN id % 2 != 0 
            THEN COALESCE(LEAD (id) OVER(ORDER BY id), id)
        ELSE LAG (id) OVER(ORDER BY id)
    END as id,
    student
FROM seat
ORDER BY id ASC