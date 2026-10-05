-- SELECT name
-- FROM salesperson
-- WHERE sales_id NOT IN (
--     SELECT sales_id
--     FROM orders
--     WHERE com_id IN (
--         SELECT com_id
--         FROM company
--         WHERE name = 'RED'
--     )
-- )

SELECT name
FROM salesperson s
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    JOIN company c
    ON o.com_id = c.com_id
    WHERE c.name = 'RED'
    AND s.sales_id = o.sales_id
)