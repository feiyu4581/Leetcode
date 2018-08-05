class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(0, rowIndex):
            row = [sum(t) for t in zip([0] + row, row + [0])]

        return row


x = Solution()
print(x.generate(4) == [1,4,6,4,1])