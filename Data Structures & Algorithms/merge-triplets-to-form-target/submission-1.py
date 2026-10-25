class Solution:

  def mergeTriplets(
      self, triplets: list[list[int]], target: list[int]
  ) -> bool:
    res = [0, 0, 0]

    for a, b, c in triplets:
      # Skip if any element overshoots the target
      if a > target[0] or b > target[1] or c > target[2]:
        continue

      # Safely take the max
      res[0] = max(res[0], a)
      res[1] = max(res[1], b)
      res[2] = max(res[2], c)

      # Early exit: found all three exact values
      if res == target:
        return True

    return res == target
