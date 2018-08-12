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
            if nums[mid] == nums[low]:
                low += 1
            elif nums[mid] == nums[high]:
                high -= 1
            elif nums[mid] > nums[low]:
                low = mid
            else:
                high = mid

        return min(nums[low], nums[0])


x = Solution()
print(x.findMin([1,3,5]) == 1)
print(x.findMin([2,2,2,0,1]) == 0)
