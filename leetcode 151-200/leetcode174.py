class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0

        dp = [float('inf')] * (len(dungeon[0]) + 1)
        dp[-2] = 1
        for row in range(len(dungeon) - 1, -1, -1):
            for col in range(len(dungeon[0]) - 1, -1, -1):
                dp[col] = max(min(dp[col], dp[col + 1]) - dungeon[row][col], 1)

        return dp[0]

x = Solution()
print(x.calculateMinimumHP([[0]]))
print(x.calculateMinimumHP([
    [-2, -3 ,3],
    [-5, -10, 1],
    [10, 30, -5]
]))

print(x.calculateMinimumHP([
    [-2, -3, 3],
    [-5, 10, 1],
    [10, 30, -5],
]))
