class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if nums[r] < target:
            return r + 1
        if nums[0] > target:
            return 0
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1
        
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid - 1] < target:
                    return mid
                r = mid
            else:
                if nums[mid + 1] > target:
                    return mid + 1
                l = mid
