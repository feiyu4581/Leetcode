class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = []
        for row in range(len(triangle) - 1, -1, -1):
            if not dp:
                for col, value in enumerate(triangle[row]):
                    dp.append((value))
            else:
                for col, value in enumerate(triangle[row]):
                    dp[col] = value + min(dp[col], dp[col + 1])

        return dp[0]


x = Solution()
print(x.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]) == 11)
