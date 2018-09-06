from collections import defaultdict

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = defaultdict(lambda: 0)
        for index in range(len(nums)):
            dp[index] = (max(
                dp[index - 2] + nums[index],
                dp[index - 3] + nums[index],
                dp[index - 1],
                nums[index],
            ))

        return dp[len(nums) - 1]



x = Solution()
print (x.rob([1,2,3,1]) == 4)
print (x.rob([2,7,9,3,1]) == 12)
