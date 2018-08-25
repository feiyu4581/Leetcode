class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers_dict = {}
        for index, number in enumerate(numbers):
            numbers_dict.setdefault(number, [])
            numbers_dict[number].append(index + 1)

        for start in range(len(numbers)):
            if target - numbers[start] in numbers_dict:
                for end in numbers_dict[target - numbers[start]]:
                    if end != start + 1:
                        return [start + 1, end]


x = Solution()
print(x.twoSum([2, 7, 11, 15], 9) == [1, 2])
print(x.twoSum([0, 0, 3, 4], 0) == [1, 2])
