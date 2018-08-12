class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negative = numerator * denominator < 0 
        numerator, denominator = abs(numerator), abs(denominator)
        res, num = divmod(numerator, denominator)
        if not num:
            return (negative and '-' or '') + str(res)

        extra = ''
        num *= 10
        cache, index = {}, 0
        while num:
            if num not in cache:
                if num >= denominator:
                    extra += str(num // denominator)
                    new_num = num % denominator * 10
                else:
                    extra += '0'
                    new_num = num * 10

                cache[num] = index
                index += 1
                num = new_num
            else:
                extra = extra[:cache[num]] + '(' + extra[cache[num]:] + ')'
                break

        return (negative and '-' or '') + str(res or 0) + '.' + extra


x = Solution()
# print(x.fractionToDecimal(1, 2) == '0.5')
# print(x.fractionToDecimal(2, 1) == '2')
# print(x.fractionToDecimal(2, 3) == '0.(6)')
# print(x.fractionToDecimal(4, 333) == '0.(012)')
# print(x.fractionToDecimal(-50, 8))
# print(x.fractionToDecimal(7, -12))
print(x.fractionToDecimal(-2147483648, 1))