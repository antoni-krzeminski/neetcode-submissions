class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def recursion(sum, curr, start_ind):
            nonlocal res
            for i in range(start_ind, len(nums) ):
                num = nums[i]
                if sum + num == target:

                    curr.append(num)

                    res.append(curr.copy())
                    curr.pop(-1)
                    continue
                if sum + num > target:
                    continue
                else:
                    curr.append(num)
                    sum += num
                    recursion(sum, curr, i)
                    curr.pop(-1)
                    sum -= num

        recursion(0, [], 0)
        return res    