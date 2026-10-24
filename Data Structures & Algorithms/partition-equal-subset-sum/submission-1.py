class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 != 0:
            return False
        sums = []
        target = sum_nums // 2
        if sum_nums % 2 != 0:
            return False
        dp = [False] * (sum_nums // 2 + 1)
        dp[0] = True
        for num in nums:
      # Iterate backwards from target down to num
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

      # Early termination: if we reached the target, stop early
            if dp[target]:
                return True

        return dp[target]

