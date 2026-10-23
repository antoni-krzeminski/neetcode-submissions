class Solution:
    def climbStairs(self, n: int) -> int:
        # [1, 2, 0, 0, 0]
        # time complexity o(n)
        # space complexity o(n)
        dp = [0] * n
        dp[0] = 1        
        
        if n == 1:
            return dp[0]
        dp[1] = 2

        if n == 2:
            return dp[1]

        if n < 1:
            return -1

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]