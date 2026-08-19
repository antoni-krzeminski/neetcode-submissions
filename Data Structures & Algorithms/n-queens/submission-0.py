class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def backtrack(board, row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if self.isPossible(board, row, col, n):
                    board[row][col] = "Q"
                    backtrack(board, row + 1)
                    board[row][col] = "."  # backtrack (undo)

        # Use list of lists so characters can be modified
        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(board, 0)
        return res

    def isPossible(self, board, r, c, n):
        # Check vertical column above
        for i in range(r):
            if board[i][c] == "Q":
                return False

        # Check top-left diagonal
        i, j = r - 1, c - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check top-right diagonal
        i, j = r - 1, c + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True
