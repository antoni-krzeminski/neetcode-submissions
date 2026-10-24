class Solution:
    def canJump(self, nums: List[int]) -> bool:
        possible = [0] * len(nums)
        possible[0] = 1
        max_jumped = 0
        for i in range(len(nums)):
            if i <= max_jumped:
                max_jumped = max(max_jumped, i + nums[i])
        return max_jumped >= len(nums) - 1
 
