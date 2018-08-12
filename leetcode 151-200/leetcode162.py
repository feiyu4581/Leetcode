class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low


x = Solution()
print(x.findPeakElement([1,2,3,1]) == 2)
print(x.findPeakElement([1,2,1,3,5,6,4]) in (1, 5))