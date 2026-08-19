
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # will store [temp, index]
        iter2 = 0

        for t in temperatures:
            while len(stack) != 0 and t > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                res[prev_index] = iter2 - prev_index

            stack.append([t, iter2])
            iter2 += 1

        return res
