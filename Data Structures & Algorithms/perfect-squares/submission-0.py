class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        x = 1
        ind = 0
        for ind in range(len(dp)):
            x = 1
            while x * x + ind < len(dp):
                if dp[ind] != 0 or ind == 0:
                    if dp[x * x + ind] != 0:
                        dp[x * x + ind] = min(dp[x * x + ind], dp[ind] + 1) 
                    else:
                        dp[x * x + ind] = dp[ind] + 1
                x += 1
        print(dp)
        return dp[-1]