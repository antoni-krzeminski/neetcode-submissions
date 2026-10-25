class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        nums = heights
        ans = 0
        while l < r:
            curr = min(nums[l], nums[r]) * (r - l)
            ans = max(ans, curr)
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        return ans
