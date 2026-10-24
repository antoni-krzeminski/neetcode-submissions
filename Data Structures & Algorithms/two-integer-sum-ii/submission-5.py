class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while True:           
            lr_sum = numbers[l] +  numbers[r]
            if lr_sum == target:
                return [l + 1, r + 1]
            if lr_sum > target:
                r = r - 1
            else:
                l += 1