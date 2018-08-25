class Solution:
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter, max_num, max_nums = {}, None, 0
        for num in nums:
            counter.setdefault(num, 0)
            counter[num] += 1

            if counter[num] > max_nums:
                max_nums, max_num = counter[num], num

        return max_num

    def majorityElement(self, nums):
        if not nums:
            return None

        nums.sort()
        return nums[len(nums) // 2]


x = Solution()
print(x.majorityElement([3,2,3]) == 3)
print(x.majorityElement([2,2,1,1,1,2,2]) == 2)
        