class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        

        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        dp[0][0] = grid[0][0]
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                left = float("inf")
                up = float("inf")
                if col != 0:
                    left = dp[row][col - 1] + grid[row][col]
                if row != 0:
                    up = dp[row - 1][col] + grid[row][col]
                dp[row][col] = min(left,up)
        return dp[m - 1][n - 1]




                




