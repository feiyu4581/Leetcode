class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict, memo = set(wordDict), {}
        def dfs(start):
            if start not in memo:
                ans = False
                if start >= len(s):
                    ans = True
                else:
                    for index in range(start, len(s)):
                        if s[start:index + 1] in wordDict and dfs(index + 1):
                            ans = True
                            break

                memo[start] = ans
            return memo[start]

        return dfs(0)


x = Solution()
print(x.wordBreak('leetcode', ["leet", "code"]) == True)
print(x.wordBreak('applepenapple', ["apple", "pen"]) == True)
print(x.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]) == False)