-- Last updated: 7/9/2026, 9:01:56 AM
SELECT 
    p.firstname,
    p.lastname,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
ON p.PersonID = a.PersonID

