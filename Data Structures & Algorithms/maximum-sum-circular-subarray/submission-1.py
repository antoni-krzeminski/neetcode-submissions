class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        right_max = [0] * len(nums)
        curr_right = 0
        max_r = min(nums)
        for i in range(len(nums) - 2, -1, -1):
            curr_right += nums[i + 1]
            max_r = max(max_r, curr_right)
            right_max[i] = max_r
        print(right_max)

        max_sum = nums[0]
        curr_sum = 0
        cum_sum = 0
        for i, num in enumerate(nums):
            # If current running sum is negative, it's dead weight — reset to 0
            if curr_sum < 0:
                curr_sum = 0
            cum_sum += num
            curr_sum += num
            max_sum = max(max_sum, curr_sum, cum_sum + right_max[i])
        return max_sum

