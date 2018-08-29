select distinct l1.Num as ConsecutiveNums FROM Logs l1, Logs l2, Logs L3
WHERE l1.Num = L2.Num and L2.Num = L3.Num and l1.Id = l2.Id - 1 and l2.id = l3.id - 1;