class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_max(normal_nums, negative_count):
            if not normal_nums:
                return 0

            if len(normal_nums) == 1:
                return normal_nums[0]

            current_negative_count, start, end, all_nums = 0, 0, 0, 1
            for num in normal_nums:
                if num < 0:
                    current_negative_count += 1

                if current_negative_count < negative_count:
                    end = (end or 1) * num

                if current_negative_count > 1 or (current_negative_count == 1 and num > 0):
                    start = (start or 1) * num

                all_nums *= num

            return max(start, end, all_nums)

        temp, max_area = [], 0 if 0 in nums else float('-inf')
        start, negative_count = None, 0
        for num in nums:
            if num == 0:
                if not start is None:
                    temp.append(start)
                max_area = max(get_max(temp, negative_count), max_area)
                temp, start, negative_count = [], None, 0
            else:
                if num > 0:
                    start = num if start is None else start * num
                else:
                    if not start is None:
                        temp.append(start)
                    temp.append(num)
                    negative_count += 1
                    start = None

        if not start is None:
            temp.append(start)

        return max(get_max(temp, negative_count), max_area)


x = Solution()
print(x.maxProduct([2,3,-2,4]) == 6)
print(x.maxProduct([-2,0,-1]) == 0)
print(x.maxProduct([-2]) == -2)
print(x.maxProduct([-3,0,1,-2]) == 1)
        