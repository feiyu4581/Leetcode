class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        row_length, col_length = len(board), len(board[0])
        
        bundarys, internals = set(), set()
        for row in range(row_length):
            for col in range(col_length):
                if board[row][col] == 'O':
                    if row == 0 or col == 0 or row == row_length - 1 or col == col_length - 1:
                        bundarys.add((row, col))
                    else:
                        internals.add((row, col))

        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while bundarys:
            row, col = bundarys.pop()
            for offset in offsets:
                next_row, next_col = row + offset[0], col + offset[1]
                if next_row < 0 or next_row >= len(board) or next_col < 0 or next_col >= len(board[0]):
                    continue

                if (next_row, next_col) in internals:
                    internals.remove((next_row, next_col))
                    bundarys.add((next_row, next_col))

        for row, col in internals:
            board[row][col] = 'X'

        return board


x = Solution()
print(x.solve([
    ["O","X","X","O","X"],
    ["X","O","O","X","O"],
    ["X","O","X","O","X"],
    ["O","X","O","O","O"],
    ["X","X","O","X","O"]
]) == [
    ["O","X","X","O","X"],
    ["X","X","X","X","O"],
    ["X","X","X","O","X"],
    ["O","X","O","O","O"],
    ["X","X","O","X","O"]
])
print(x.solve([
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]) == [
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X']
])
        