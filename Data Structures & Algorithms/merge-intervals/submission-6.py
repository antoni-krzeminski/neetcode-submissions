class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr_interval = intervals[0]
        output = []
        for i in range(1, len(intervals)):
            if curr_interval[1] >= intervals[i][0]:
                curr_interval[1] = max(curr_interval[1], intervals[i][1])
            else:
                output.append(curr_interval)
                curr_interval = intervals[i]

        output.append(curr_interval)
        return output
