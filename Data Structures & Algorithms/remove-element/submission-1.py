class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[i]
                nums[i] = nums[index]
                nums[index] = temp
                index += 1
                k += 1
        return k
