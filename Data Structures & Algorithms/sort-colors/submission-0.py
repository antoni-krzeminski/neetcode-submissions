class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        r = 0
        b = len(nums) - 1

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = nums[r]
                nums[r] = 0
                r += 1
        print(nums)


        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                nums[i] = nums[b]
                nums[b] = 2
                b -= 1
        