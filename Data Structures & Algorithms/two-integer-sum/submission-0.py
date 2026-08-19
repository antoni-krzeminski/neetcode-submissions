class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        iter = 0
        for x in nums:
            if x in hash:
                return [hash[x], iter]
                

            hash[target - x] = iter
            iter += 1
        return [1,2]

