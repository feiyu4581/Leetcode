class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            x = 1 << i
            i_sum = 0
            for num in nums:
                if x & num:
                    i_sum += 1

            if i_sum % 3 != 0:
                res = res | x

        if res >= 2 ** 31:
            res -= 2 ** 32
        return res


x = Solution()
print(x.singleNumber([2,2,3,2]) == 3)
print(x.singleNumber([0,1,0,1,0,1,99]) == 99)
print(x.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
        