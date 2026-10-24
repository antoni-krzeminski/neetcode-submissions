class Solution:

  def singleNumber(self, nums: list[int]) -> int:
    singles = set()

    for num in nums:
      if num not in singles:
        singles.add(num)
      else:
        singles.remove(num)

    return singles.pop()
