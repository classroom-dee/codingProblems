WITH 
personnel
AS (
    SELECT e.name as Employee, e.salary as Salary, d.name AS Department
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id
),
ranked
AS (
    SELECT
        Department,
        Employee,
        Salary,
        DENSE_RANK () OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM personnel
)
SELECT Department, Employee, Salary
FROM ranked
WHERE rnk <= 3