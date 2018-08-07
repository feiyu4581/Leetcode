class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_area = 0
        for num in nums:
            if num - 1 not in nums:
                current_num = num + 1
                current_sequence = 1
                while current_num in nums:
                    current_num += 1
                    current_sequence += 1

                max_area = max(max_area, current_sequence)

        return max_area


x = Solution()
print(x.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
        