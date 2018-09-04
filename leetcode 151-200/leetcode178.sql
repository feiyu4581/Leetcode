# Write your MySQL query statement below
select Score, (
    SELECT COUNT(*) + 1 FROM
        (SELECT DISTINCT Score FROM Scores) as distinct_score
    WHERE scores.Score < distinct_score.Score
) AS Rank from Scores scores
ORDER BY Score DESC;
