class Solution:

  def coinChange(self, coins: list[int], amount: int) -> int:
    # Use amount + 1 as infinity since max possible coins cannot exceed amount (if coin=1)
    max_val = amount + 1
    dp = [max_val] * (amount + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    for i in range(1, amount + 1):
      for coin in coins:
        if i - coin >= 0:
          dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != max_val else -1
