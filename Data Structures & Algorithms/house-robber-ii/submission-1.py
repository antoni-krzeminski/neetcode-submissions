class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def rob_linear(houses: list[int]) -> int:
            prev2, prev1 = 0, 0
            for money in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + money)
            return prev1

        # We can't rob both the first and last house:
        # Case 1: Exclude the last house
        # Case 2: Exclude the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
