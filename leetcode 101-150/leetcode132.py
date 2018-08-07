from collections import defaultdict

class Solution:
    def minCut(self, s):
        if not s:
            return False

        palin = [[False] * len(s) for _ in range(len(s))]
        cuts = list(range(len(s)))
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j <= 1 or palin[i - 1][j + 1]):
                    palin[i][j] = True
                    if j == 0:
                        cuts[i] = 0
                    elif cuts[i] > cuts[j - 1] + 1:
                        cuts[i] = cuts[j - 1] + 1

        return cuts[-1]


    def minCut2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        queue = [(index, index) for index in range(len(s))]
        seen = set()
        graph = defaultdict(list)
        while queue:
            i, j = queue.pop()
            if (i, j) in seen:
                continue

            graph[i].append((i, j))
            seen.add((i, j))

            if i == j:
                if i - 1 >= 0 and s[i] == s[i - 1]:
                    queue.append((i - 1, j))
                if i + 1 < len(s) and s[i + 1] == s[i]:
                    queue.append((i, i + 1))

            if i - 1 >= 0 and j + 1 < len(s) and s[i - 1] == s[j + 1]:
                queue.append((i - 1, j + 1))

        print ('-------', len(seen))
        cache = {}
        def dfs(i, j):
            if (i, j) not in cache:
                if (i, j) in seen:
                    ans = 1
                elif j - i == 1:
                    ans = 2
                else:
                    ans = float('inf')
                    for index in range(i, j):
                        ans = min(dfs(i, index) + dfs(index + 1, j), ans)
                        if ans <= 2:
                            break

                cache[i, j] = ans
            else:
                print ('get')

            return cache[i, j]

        return dfs(0, len(s) - 1) - 1


x = Solution()
print(x.minCut('aab') == 1)
print(x.minCut('ab'))
print(x.minCut('cdd'))
print(x.minCut('leet'))
print(x.minCut(
"apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
))

# print(x.minCut('ababababababababababababcbabababababababababababa'))
        