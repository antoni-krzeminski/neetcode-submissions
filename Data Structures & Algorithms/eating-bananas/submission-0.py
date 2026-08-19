class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 1
        while k > 0:
            hrs = 0
            for x in piles:
                if x % k == 0:
                    hrs += x // k
                else:
                    hrs += x // k + 1
            if hrs <= h:
                return k
            k += 1