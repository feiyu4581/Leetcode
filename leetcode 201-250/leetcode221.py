class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        M, N, sideLen = len(matrix), len(matrix[0]), [[1 if ch == '1' else 0 for ch in row] for row in matrix]

        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == '1':
                    sideLen[i][j] = 1 + min(sideLen[i - 1][j], sideLen[i][j - 1], sideLen[i - 1][j - 1])

        return max(max(row) for row in sideLen) ** 2

    def maximalSquare2(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_area = 0
        areas = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        def dfs(row, col):
            if row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == '0':
                return 0

            if areas[row][col] == 0:
                length = 1
                while length < len(matrix):
                    for offset in range(length + 1):
                        left = dfs(row + length, col + offset)
                        bottom = dfs(row + offset, col + length)
                        if left < 1 or bottom < 1:
                            areas[row][col] = length
                            return length

                    length += 1

                areas[row][col] = length

            return areas[row][col]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    max_area = max(dfs(row, col), max_area)

        return max_area ** 2


x = Solution()
print(x.maximalSquare([
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]) == 4)

print(x.maximalSquare([
    ['1', '1', '1', '1'],
    ['1', '1', '1', '1'],
    ['1', '1', '1', '1']
]) == 9)
