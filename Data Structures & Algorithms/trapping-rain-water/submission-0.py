class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        LM = height[0]
        res = 0
        RM = height[r]
        while l < r:
            if LM < RM:
                l += 1
                LM = max(height[l], LM)
                res += LM - height[l]
            else:
                r -= 1
                RM = max(height[r], RM)
                res += RM - height[r]
        return res