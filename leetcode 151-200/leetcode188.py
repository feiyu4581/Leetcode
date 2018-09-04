class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        if k >= len(prices) / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)

        dp_1, dp_2 = [0] * len(prices), [0] * len(prices)
        for num in range(1, k + 1):
            buy = prices[0]
            for index in range(1, len(prices)):
                dp_2[index] = max(dp_2[index - 1], prices[index] - buy)
                buy = min(buy, prices[index] - dp_1[index])

            dp_1 = dp_2
            dp_2 = [0] * len(prices)
                
        return dp_1[-1]


x = Solution()
print(x.maxProfit(2, [3,2,6,5,0,3]) == 7)
