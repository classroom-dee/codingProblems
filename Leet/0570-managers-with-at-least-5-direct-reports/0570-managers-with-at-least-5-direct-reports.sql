SELECT manager.name
FROM Employee manager
JOIN Employee teammate
ON manager.id = teammate.managerId
GROUP BY manager.id
HAVING COUNT(*) > 4