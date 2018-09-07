class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        diff = m ^ n
        if not diff:
            return m

        sequence = None
        for index in range(31, -1, -1):
            if diff & (1 << index):
                sequence = index
                break

        flag = int(('0' * sequence).rjust(32, '1'), 2)

        return m & flag


x = Solution()
print(x.rangeBitwiseAnd(5, 7) == 4)
print(x.rangeBitwiseAnd(0, 1) == 0)
