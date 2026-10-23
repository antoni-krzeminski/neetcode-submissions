class Solution:
    def rob(self, nums: List[int]) -> int:
        # we will count max stolen money for each house by dp
        # O(n) time complexity
        # O(n) space complexity 

        n = len(nums)
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
  
        return dp[-1]