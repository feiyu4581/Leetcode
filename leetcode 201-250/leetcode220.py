from collections import defaultdict

class Solution:
    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        counter = defaultdict(list)
        for index in range(len(nums)):
            for offset in range(t + 1):
                current = counter[nums[index] + offset]
                if current and current[-1] + k >= index:
                    return True

                current.append(index)

        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets = {}
        for i, v in enumerate(nums):
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            bucketNum, offset = (v // t, 1) if t else (v, 0)
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # Remove the bucket which is too far away. Beware of zero t.
                del buckets[nums[i - k] // t if t else nums[i - k]]

        return False

    def test(self, nums, k):
        buckets = {}
        for i, v in enumerate(nums):
            if v in buckets and buckets[v] == v:
                return True

            buckets[v] = v
            if len(buckets) > k:
                del buckets[nums[i - k]]

        return False


x = Solution()
print(x.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) == True)
print(x.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2) == True)
print(x.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) == False)
print(x.containsNearbyAlmostDuplicate([0, 2147483647], 1, 2147483647) == True)
