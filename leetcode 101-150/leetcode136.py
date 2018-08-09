class Solution(object):
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return seen.pop()

    def singleNumber(self, nums):
        if not nums:
            return

        res = 0
        for num in nums:
            res = res ^ num

        return res


x = Solution()
# print(x.singleNumber([2,2,1]) == 1)
# print(x.singleNumber([4,1,2,1,2]) == 4)
# print(x.singleNumber([1,3,1,-1,3]) == -1)
print(x.singleNumber([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]) == 16)
        