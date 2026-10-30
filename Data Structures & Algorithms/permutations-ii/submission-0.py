class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)


        res = []

        def backtrack(comb):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    comb.append(num)
                    backtrack(comb)
                    counter[num] += 1
                    comb.pop()
        
        backtrack([])
        return res