class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = ""
        maxlen = 0
        for i in range(len(s)):
            if s[i] not in curr:
                curr += s[i]
                maxlen = max(len(curr), maxlen)
            else:
                for j in range(len(curr)):
                    if curr[j] == s[i]:
                        curr = curr[j+1:] + s[i]
                        break

        return maxlen