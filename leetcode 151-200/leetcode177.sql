CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct a.salary from employee as a
      where (N - 1) = (
          select count(distinct b.salary) from employee as b 
          where b.salary > a.salary) 
  );
END





CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      
      SELECT (
        SELECT DISTINCT Salary FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET N
      ) AS NthHighestSalary
      
  );
END