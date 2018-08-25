import string
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_maps = {
            char: index
            for index, char in enumerate(string.ascii_uppercase, 1)
        }

        carry, res = 0, 0
        for char in reversed(s):
            res += letter_maps[char] * (26 ** carry) 
            carry += 1
 
        return res


x = Solution()
print(x.titleToNumber('A') == 1)
print(x.titleToNumber('AB') == 28)
print(x.titleToNumber('ZY') == 701)
