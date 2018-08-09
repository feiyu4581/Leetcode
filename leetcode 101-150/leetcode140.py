class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict, memo = set(wordDict), {}
        def dfs(start):
            if start not in memo:
                ans = []
                if start >= len(s):
                    ans = [[]]
                else:
                    for index in range(start, len(s)):
                        if s[start:index + 1] in wordDict:
                            for word in dfs(index + 1):
                                ans.append([s[start:index + 1]] + word)

                memo[start] = ans
            return memo[start]

        return list(map(lambda item: ' '.join(item), dfs(0)))


x = Solution()
print(x.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]) == [
  "cats and dog",
  "cat sand dog"
])
        
print(x.wordBreak('pineapplepenapple', ["apple", "pen", "applepen", "pine", "pineapple"]) == [
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
])

print(x.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]) == [])