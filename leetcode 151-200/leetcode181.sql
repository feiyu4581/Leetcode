# Write your MySQL query statement below
SELECT employee.Name AS Employee FROM Employee employee
  INNER JOIN Employee manager ON employee.ManagerId = manager.id
WHERE employee.Salary > manager.Salary;



select e2.Name Employee
from employee e1, employee e2
where e1.Id = e2.ManagerId and e1.Salary < e2.Salary