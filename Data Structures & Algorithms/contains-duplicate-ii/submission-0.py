class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()

        l = 0

        for R in range(len(nums)):
            if R - l > k:
                window.remove(nums[l])
                l += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False