-- Last updated: 7/9/2026, 9:01:44 AM
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;