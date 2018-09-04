/* Write your T-SQL query statement below */
SELECT Department, Employee, Salary FROM (
    SELECT
        Department.Name AS Department,
        Employee.Name AS Employee,
        Employee.Salary AS Salary,
        DENSE_RANK () OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) as ranking
    FROM Employee
        INNER JOIN Department ON Employee.DepartmentId = Department.Id
) AS Employee WHERE Employee.ranking < 4
ORDER BY Department, Salary Desc;