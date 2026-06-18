-- WITH cnt_by_cust AS
-- (
--     SELECT customer_number, COUNT(*) AS cnt
--     FROM orders
--     GROUP BY customer_number
-- )
-- SELECT customer_number
-- FROM cnt_by_cust
-- ORDER BY cnt DESC
-- LIMIT 1

SELECT customer_number
FROM orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1