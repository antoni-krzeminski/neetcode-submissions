class Solution:

  def numDecodings(self, s: str) -> int:
    if not s or s[0] == "0":
      return 0

    n = len(s)
    # dp[i] stores number of ways to decode s[:i]
    dp = [0] * (n + 1)

    # Base cases:
    dp[0] = 1  # Empty prefix has 1 valid way (acts as neutral element for 2-digit pairs)
    dp[1] = 1  # First char is guaranteed non-zero due to guard check

    for i in range(2, n + 1):
      one_digit = s[i - 1]
      two_digits = s[i - 2 : i]

      # Check 1-digit jump (1 to 9)
      if one_digit != "0":
        dp[i] += dp[i - 1]

      # Check 2-digit jump (10 to 26)
      if "10" <= two_digits <= "26":
        dp[i] += dp[i - 2]

    return dp[n]
