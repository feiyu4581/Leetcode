from collections import defaultdict

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
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

        res = []
        temp = []
        def dfs(index):
            if index >= len(s):
                res.append(temp[:])
            else:
                for next_word in graph[index]:
                    temp.append(s[next_word[0]:next_word[1] + 1])
                    dfs(next_word[1] + 1)
                    temp.pop()

        dfs(0)
        return res


x = Solution()
print(x.partition('aab') == [
    ["aa","b"],
    ["a","a","b"]
])
