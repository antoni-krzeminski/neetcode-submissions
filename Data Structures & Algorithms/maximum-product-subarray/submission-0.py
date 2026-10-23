class Solution:

  def maxProduct(self, nums: list[int]) -> int:
    # Initialize all trackers to the first element
    global_max = nums[0]
    curr_max = nums[0]
    curr_min = nums[0]

    for num in nums[1:]:
      # Store candidates to avoid overwriting curr_max prematurely
      cand1 = curr_max * num
      cand2 = curr_min * num

      curr_max = max(num, cand1, cand2)
      curr_min = min(num, cand1, cand2)

      global_max = max(global_max, curr_max)

    return global_max
