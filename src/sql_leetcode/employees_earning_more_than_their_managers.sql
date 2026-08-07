SELECT e.name as Employee From Employee e
JOIN Employee m 
ON e.managerId = m.id
Where e.salary > m.salary;
