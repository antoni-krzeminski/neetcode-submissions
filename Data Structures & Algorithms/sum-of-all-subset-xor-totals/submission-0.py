class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(index, subset):
            xorr = 0
            nonlocal res
            for num in subset:
                xorr ^= num
            res += xorr

            for j in range(index, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()


        backtrack(0, [])
        return res