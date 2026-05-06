-- SELECT co.name AS Customers
-- FROM
-- (
--     SELECT o.id, c.name
--     FROM customers c
--     LEFT JOIN orders o
--     ON c.id = o.customerId
--     HAVING o.id is Null
-- ) as co

-- SELECT c.name AS Customers
-- FROM customers c
-- LEFT JOIN orders o
--     ON c.id = o.customerId
-- WHERE o.id IS NULL

SELECT c.name AS Customers
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customerId = c.id
)