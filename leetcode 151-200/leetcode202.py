class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        exists = set()
        while n != 1:
            if n in exists:
                return False

            exists.add(n)
            new_value = 0
            for num in str(n):
                new_value += int(num) ** 2

            n = new_value

        return True

x = Solution()
# print(x.isHappy(19) == True)
print(x.isHappy(2))
