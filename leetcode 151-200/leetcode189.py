class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or not k:
            return

        length, start_index = len(nums), 0
        current_value, current_index = nums[0], 0
        for _ in range(len(nums)):
            next_index = (current_index + k) % length
            next_value = nums[next_index]

            nums[next_index] = current_value
            if next_index == start_index:
                start_index += 1
                if start_index >= length:
                    break
                current_value, current_index = nums[start_index], start_index
            else:
                current_value, current_index = next_value, next_index

        return nums


x = Solution()
# print (x.rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4])
# print (x.rotate([-1,-100,3,99], 2) == [3,99,-1,-100])
print (x.rotate([1], 1) == [1])

        