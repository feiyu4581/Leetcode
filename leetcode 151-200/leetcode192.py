class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for index in range(32):
            if n & (1 << index):
                count += 1

        return count


x = Solution()
print(x.hammingWeight(11) == 3)
print(x.hammingWeight(128) == 1)
