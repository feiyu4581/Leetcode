class Solution(object):
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_area = max(prices[j] - prices[i], max_area)

        return max_area
    
    def maxProfit3(self, prices):
        diff = []
        for index in range(1, len(prices)):
            diff.append(prices[index] - prices[index - 1])

        areas, res = [], 0
        for value in diff:
            if value > 0:
                res += value
            else:
                res = max(res + value, 0)

            areas.append(res)

        if areas:
            return max(areas)

        return 0

    def maxProfit(self, prices):
        if not prices:
            return 0

        min_value, max_area = prices[0], 0
        for value in prices[1:]:
            if value < min_value:
                min_value = value

            max_area = max(max_area, value - min_value)

        return max_area


x = Solution()
print(x.maxProfit([7,1,5,3,6,4]) == 5)
print(x.maxProfit([7,6,4,3,1]) == 0)
print(x.maxProfit([1, 2]) == 1)
