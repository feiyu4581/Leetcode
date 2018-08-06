import string
from collections import defaultdict, OrderedDict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        memo = {}
        def find_next(word):
            if word not in memo:
                next_words = []
                for index in range(len(word)):
                    for char in string.ascii_lowercase:
                        new_word = word[:index] + char + word[index + 1:]
                        if new_word != word and new_word in wordList:
                            next_words.append(new_word)

                memo[word] = next_words
            return memo[word]

        def bfs():
            queue = [beginWord]
            distance = defaultdict(lambda: float('inf'))
            parents = defaultdict(list)

            distance[beginWord] = 0
            while queue:
                word = queue.pop(0)
                if word == endWord:
                    return parents

                for next_word in find_next(word):
                    if distance[word] + 1 < distance[next_word]:
                        distance[next_word] = distance[word] + 1
                        parents[next_word] = [word]
                        queue.append(next_word)
                    elif distance[word] + 1 == distance[next_word]:
                        parents[next_word].append(word)

            return None

        def dfs(parents):
            paths = []
            stack = [(endWord, [endWord])]
            while stack:
                word, path = stack.pop()
                if word == beginWord:
                    paths.append(path)
                else:
                    for next_word in parents[word]:
                        stack.append((next_word, [next_word] + path))

            return paths


        wordList = set(wordList)
        parents = bfs()
        if not parents:
            return []

        paths = dfs(parents)
        return paths
        


x = Solution()
print(x.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]) == [
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
])
        