class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        for i in range(32):
            radix = 1 << i
            nums = list(filter(lambda num: num & radix == 0, nums)) + list(filter(lambda num: num & radix != 0, nums))

        max_area = 0
        for index in range(len(nums) - 1):
            max_area = max(max_area, nums[index + 1] - nums[index])

        return max_area

x = Solution()
print(x.maximumGap([3,6,9,1]) == 3)
print(x.maximumGap([10]) == 0)
