class Solution(object):
    def generate2(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []

        res = [[1]]
        for cycle in range(1, numRows):
            temp = []
            for index in range(0, cycle + 1):
                if 0 < index < cycle:
                    value = res[cycle - 1][index] + res[cycle - 1][index -1]
                else:
                    value = 1

                temp.append(value)

            res.append(temp)
        return res

    def generate(self, numRows):
        row, res = [1], []
        for _ in range(numRows):
            res.append(row)
            row = [sum(t) for t in zip([0] + row, row + [0])]

        return res


x = Solution()
print(x.generate(5) == [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
])