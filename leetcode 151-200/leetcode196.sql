# Write your MySQL query statement below
DELETE person_a FROM Person as person_a
  INNER JOIN Person  AS person_b ON person_b.Id < person_a.Id AND person_b.Email = person_a.Email;
