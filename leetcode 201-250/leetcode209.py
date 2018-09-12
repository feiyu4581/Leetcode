class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        current_sum, start, min_length = 0, 0, float('inf')
        for index in range(len(nums)):
            current_sum += nums[index]
            while current_sum >= s:
                min_length = min(index - start + 1, min_length)
                current_sum -= nums[start]
                start += 1

        return 0 if min_length == float('inf') else min_length


x = Solution()
print(x.minSubArrayLen(7, [2,3,1,2,4,3]) == 2)
print(x.minSubArrayLen(30, [2,3,1,2,4,3]) == 0)
        