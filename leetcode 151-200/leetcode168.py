import string

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        numbers = string.ascii_uppercase
        def convert(number):
            if number <= 25:
                return numbers[number]
            else:
                return convert(number // 26 - 1) + convert(number % 26)

        return convert(n - 1)


x = Solution()
print(x.convertToTitle(1) == 'A')
print(x.convertToTitle(28) == 'AB')
print(x.convertToTitle(52) == 'AZ')
print(x.convertToTitle(701) == 'ZY')
        