WITH fact
AS (
    SELECT t.id, t.request_at, t.status
    FROM trips t
    JOIN users client
    ON (t.client_id = client.users_id AND client.role = 'client')
    JOIN users driver
    ON (t.driver_id = driver.users_id AND driver.role = 'driver')
    WHERE client.banned = 'No' AND driver.banned = 'No' AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'

)
SELECT 
    request_at AS Day, 
    ROUND(COUNT(CASE WHEN status LIKE 'cancel%' THEN 1 ELSE NULL END) / COUNT(*), 2) AS 'Cancellation Rate'
FROM fact
GROUP BY request_at
