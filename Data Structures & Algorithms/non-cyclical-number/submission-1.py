class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        while True:
            sum_sq = 0
            for s in str(n):
                sum_sq += int(s)**2
            if sum_sq == 1:
                return True
            if sum_sq in results:
                return False
            n = sum_sq
            results.add(sum_sq)
