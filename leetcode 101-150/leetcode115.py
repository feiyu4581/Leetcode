class Solution:
    def numDistinct2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        distination_length, target_length, memo = len(s), len(t), {}
        def distinct(distination_index, target_index):
            if (distination_index, target_index) not in memo:
                ans = 0
                if target_index >= target_length:
                    ans = 1

                elif distination_length - distination_index < target_length - target_index:
                    ans = 0
                else:
                    if s[distination_index] == t[target_index]:
                        ans += distinct(distination_index + 1, target_index + 1)
                    
                    ans += distinct(distination_index + 1, target_index)

                memo[distination_index, target_index] = ans

            return memo[distination_index, target_index]

        return distinct(0, 0)

    def numDistinct(self, s, t):
        dp = [
            [0 for j in range(len(t) + 1)]
            for i in range(len(s) + 1)
        ]
        for i in range(len(s)):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[len(s)][len(t)]


x = Solution()
print(x.numDistinct('rabbbit', 'rabbit') == 3)
print(x.numDistinct('babgbag', 'bag') == 5)
print(x.numDistinct('aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe',
'bddabdcae') == 10582116)