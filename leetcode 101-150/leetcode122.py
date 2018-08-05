class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff = []
        for index in range(1, len(prices)):
            diff.append(prices[index] - prices[index - 1])

        areas, res = [], 0
        for value in diff:
            if value > 0:
                res += value
            else:
                areas.append(res)
                res = 0

        areas.append(res)
        return sum(areas)


x = Solution()
print(x.maxProfit([7,1,5,3,6,4]) == 7)
print(x.maxProfit([1,2,3,4,5]) == 4)
print(x.maxProfit([7,6,4,3,1]) == 0)
