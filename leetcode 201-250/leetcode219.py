from collections import defaultdict

class Solution:
    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        counter = defaultdict(list)
        for index in range(len(nums)):
            if nums[index] in counter:
                if counter[nums[index]][-1] + k >= index:
                    return True

            counter[nums[index]].append(index)

        return False

    def containsNearbyDuplicate(self, nums, k):
        windows = set()
        for i, num in enumerate(nums):
            if num in windows:
                return True

            windows.add(num)
            if len(windows) > k:
                windows.remove(nums[i - k])

        return False


x = Solution()
print(x.containsNearbyDuplicate([1,2,3,1], 3) == True)
print(x.containsNearbyDuplicate([1,0,1,1], 1) == True)
print(x.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False)
