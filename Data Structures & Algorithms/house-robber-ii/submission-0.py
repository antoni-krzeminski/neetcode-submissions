class Solution:
    def rob(self, nums: List[int]) -> int:
        # there would be a possibility to make it O(1) space complexity by just keeping two variables for 
        # last two houses
        # my approach would be to make house robber 1 twice (one with 1st and without last house and second
        # with last hosue and without first)

        n = len(nums)
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)


        # skip the last house by iterating till n - 1
        dp = [0] * (n - 1)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])


        # skip the first house 
        dp2 = [0] * (n - 1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[2], nums[1])
        
        for i in range(2, n - 1):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i + 1])

        
        # we chose the better option out of two dp walks
        return(max(dp[-1], dp2[-1]))

