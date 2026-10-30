class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force to go for both sides
        resindex = 0
        reslen = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if reslen < j - i + 1:
                        reslen = j - i + 1
                        resindex = i
        return s[resindex : resindex + reslen]