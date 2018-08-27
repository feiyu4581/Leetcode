# Write your MySQL query statement below
SELECT FirstName, LastName, City, address.State FROM Person
    LEFT JOIN Address ON Address.PersonId = Person.PersonId;