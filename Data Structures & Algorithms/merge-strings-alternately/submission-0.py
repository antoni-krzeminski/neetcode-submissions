class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i = 0
        while len(word1) > i and len(word2) > i:
            ans.append(word1[i])
            ans.append(word2[i])
            i += 1
        
        if len(word1) == i and len(word2) != i:
            return "".join(ans) + word2[i:]
        if len(word1) > i:
            return "".join(ans) + word1[i:]
        return "".join(ans)
        


