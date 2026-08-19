class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for x in nums:
            hash.add(x)

        if len(hash) == len(nums):
            return False
        return True