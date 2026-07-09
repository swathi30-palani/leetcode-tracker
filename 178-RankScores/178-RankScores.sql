-- Last updated: 7/9/2026, 9:01:50 AM
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores;