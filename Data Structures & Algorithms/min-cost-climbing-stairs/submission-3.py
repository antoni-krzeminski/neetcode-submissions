class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]

        DP = [0] * n

        DP[0] = cost[0]
        DP[1] = cost[1]
        for i in range(2, n):
            DP[i] = min(DP[i - 1], DP[i - 2]) + cost[i]
        return min(DP[-1], DP[-2])
        