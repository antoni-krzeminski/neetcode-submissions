class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for num2 in prices[i:]:
                res = max(res, num2 - prices[i])
        return res