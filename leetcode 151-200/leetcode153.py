class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        low, high = 0, len(nums) - 1
        while low < high:
            if low + 1 == high:
                return min(nums[high], nums[low], nums[0])

            mid = (low + high) // 2
            if nums[mid] > nums[low]:
                low = mid
            else:
                high = mid

        return min(nums[low], nums[0])


x = Solution()
# print(x.findMin([3,4,5,1,2]) == 1)
# print(x.findMin([4,5,6,7,0,1,2]) == 0)
print(x.findMin([1, 2]) == 1)
