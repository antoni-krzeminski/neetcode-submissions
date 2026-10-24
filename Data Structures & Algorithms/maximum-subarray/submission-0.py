class Solution:

  def maxSubArray(self, nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
      # If current running sum is negative, it's dead weight — reset to 0
      if curr_sum < 0:
        curr_sum = 0

      curr_sum += num
      max_sum = max(max_sum, curr_sum)

    return max_sum
