class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, end = 0, len(nums)
        k = end - k
        while start < end:
            index = self.partition(nums, start, end)
            if index == k:
                return nums[index]
            elif index < k:
                start = index + 1
            else:
                end = index

    def recrusive_kth_largest(self, nums, start, end):
        if end - start > 1:
            index = self.partition_two(nums, start, end)
            self.recrusive_kth_largest(nums, start, index)
            self.recrusive_kth_largest(nums, index + 1, end)

    def partition(self, nums, start, end):
        current = start
        for index in range(start + 1, end):
            if nums[index] < nums[start]:
                current += 1
                nums[index], nums[current] = nums[current], nums[index]

        nums[current], nums[start] = nums[start], nums[current]
        return current

    def partition_two(self, nums, start, end):
        temp = nums[start]
        left, right = start, end - 1
        while left < right:
            while left < right and nums[right] >= nums[start]:
                right -= 1

            while left < right and nums[left] <= nums[start]:
                left += 1

            nums[left], nums[right] = nums[right], nums[left]

        nums[left], nums[start] = temp, nums[left]
        return left


x = Solution()

print(x.findKthLargest([2, 1], 2) == 1)
print(x.findKthLargest([3,2,1,5,6,4], 2) == 5)
print(x.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4)
        