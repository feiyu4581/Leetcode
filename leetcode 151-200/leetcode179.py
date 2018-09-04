class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a,b):
            return int(b + a) - int(a + b)

        nums = sorted([str(x) for x in nums],cmp = compare)
        ans = ''.join(nums).lstrip('0')

        return ans or '0'

x = Solution()
print(x.largestNumber([10,2]) == '210')
print(x.largestNumber([3,30,34,5,9]) == '9534330')
