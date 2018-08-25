class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n >= 5:
            res += n // 5
            n = n // 5

        return res

x = Solution()
# print(x.trailingZeroes(3) == 0)
# print(x.trailingZeroes(5) == 1)
print(x.trailingZeroes(25))
print(x.trailingZeroes(625) == 156)
        