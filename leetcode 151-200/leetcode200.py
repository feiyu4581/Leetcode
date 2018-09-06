class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count, flags = 0, set()
        row_length, col_length = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def start_bfs(row, col):
            stacks = [(row, col)]
            while stacks:
                row, col = stacks.pop()
                for direction in directions:
                    new_row, new_col = row + direction[0], col + direction[1]
                    if 0 <= new_row < row_length and 0 <= new_col < col_length and (new_row, new_col) not in flags and grid[new_row][new_col] == '1':
                        flags.add((new_row, new_col))
                        stacks.append((new_row, new_col))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    if (row, col) not in flags:
                        count += 1
                        start_bfs(row, col)

        return count


x = Solution()
print (x.numIslands([
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]) == 1)

print (x.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]) == 3)

# print (x.numIslands([
#     [1, 1, 1, 1, 0],
#     [1, 1, 0, 1, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]) == 1)

# print (x.numIslands([
#     [1, 1, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 1]
# ]) == 3)
