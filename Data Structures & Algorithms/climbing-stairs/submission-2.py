class Solution:
    def climbStairs(self, n: int) -> int:
        # [1, 2, 0, 0, 0]
        # time complexity o(n)
        # space complexity o(1)
        if n <= 0:
            return 0
        if n <= 2:
            return n
        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
    
        return prev1