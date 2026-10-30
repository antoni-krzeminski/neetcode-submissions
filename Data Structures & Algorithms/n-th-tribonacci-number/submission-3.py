class Solution:
    def tribonacci(self, n: int) -> int:
        ghost1 = 0
        ghost2 = 1
        ghost3 = 1
        curr_sum = 1
        for i in range(n - 2):
            curr_sum = ghost1 + ghost2 + ghost3
            ghost1 = ghost2
            ghost2= ghost3
            ghost3 = curr_sum
        return curr_sum if n != 0 else 0 
