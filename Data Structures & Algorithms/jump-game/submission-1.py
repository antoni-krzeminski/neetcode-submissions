class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_jumped = 0
        for i in range(len(nums)):
            if i <= max_jumped:
                max_jumped = max(max_jumped, i + nums[i])
        return max_jumped >= len(nums) - 1
 
