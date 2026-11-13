class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxlen = 1
        curr_len = 1
        prev_sign = 0  # 1: '>', -1: '<', 0: '='

        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                curr_len = curr_len + 1 if prev_sign == -1 else 2
                prev_sign = 1
            elif arr[i] < arr[i + 1]:
                curr_len = curr_len + 1 if prev_sign == 1 else 2
                prev_sign = -1
            else:
                curr_len = 1
                prev_sign = 0

            maxlen = max(maxlen, curr_len)

        return maxlen
