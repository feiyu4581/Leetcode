class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(res, [], k, n, 1)
        return res

    def dfs(self, res, current, k, n, start):
        if len(current) > k or sum(current) > n:
            return False

        if len(current) == k and sum(current) == n:
            res.append(current[:])
        else:
            for index in range(start, 10):
                if index not in current:
                    current.append(index)
                    self.dfs(res, current, k, n, index + 1)
                    current.pop()


x = Solution()
print(x.combinationSum3(3, 7) == [[1, 2, 4]])
print(x.combinationSum3(3, 9) == [[1,2,6], [1,3,5], [2,3,4]]) 
        