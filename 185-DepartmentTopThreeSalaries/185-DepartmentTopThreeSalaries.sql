-- Last updated: 7/9/2026, 9:01:39 AM
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT
        *,
        DENSE_RANK() OVER (
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS rk
    FROM Employee
) e
JOIN Department d
    ON e.departmentId = d.id
WHERE rk <= 3;