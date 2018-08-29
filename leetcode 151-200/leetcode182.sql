-- >= 2 比 > 1 慢很多
SELECT Email FROM Person
GROUP BY Email HAVING COUNT(*) > 1;