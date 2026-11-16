class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = []
        maxes = []
        minnum = max(prices)
        maxnum = 0
        for num in prices:
            minnum = min(minnum, num)
            mins.append(minnum)
        for num in prices[::-1]:
            maxnum = max(maxnum, num)
            maxes.append(maxnum)
        maxes = maxes[::-1]
        ans = 0
        print(mins, maxes)
        for i in range(len(prices) - 1):
            stonks = maxes[i + 1] - mins[i]
            ans = max(ans, stonks)
        return ans