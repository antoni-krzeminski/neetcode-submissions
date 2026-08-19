class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max = 1
        if len(nums) == 0:
            return 0
        act = 1
        nums.sort()
        nums = list(set(nums))
        nums.sort()
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1] or nums[i] - 1 == nums[i+1]:
                act += 1
                if act > max:
                    max = act
            else:
                act = 1
        return max