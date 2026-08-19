class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(sum, used, curr, start_ind):
            if sum == target:
                

                res.append(curr)
                return  
            
            for i in range(start_ind, len(candidates)):
                # Skip duplicate elements at the same tree level
                if i > start_ind and candidates[i] == candidates[i - 1]:
                    continue

                if used[i] == False and sum + candidates[i] <= target:
                    newused = used.copy()
                    newused[i] = True
                    newcurr = curr.copy()
                    newcurr.append(candidates[i])
                    backtrack(sum + candidates[i], newused, newcurr, i + 1)
        used = []

        for i in range(len(candidates)):
            used.append(False)
        backtrack(0, used, [], 0)
        return res