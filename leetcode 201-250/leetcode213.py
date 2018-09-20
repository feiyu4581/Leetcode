from collections import defaultdict

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return sum(nums)

        return max(self.max_rob(nums, 0, len(nums) - 1), self.max_rob(nums, 1, len(nums)))

    def max_rob(self, nums, start, end):
        dp = defaultdict(lambda: 0)
        for index in range(start, end):
            dp[index] = max(
                dp[index - 2] + nums[index],
                dp[index - 3] + nums[index],
                dp[index - 1],
                nums[index],
            )

        return dp[end - 1]


x = Solution()
print(x.rob([2,3,2]) == 3)
print(x.rob([1,2,3,1]) == 4)
print(x.rob([1]) == 1)
print(x.rob([1, 2]) == 2)