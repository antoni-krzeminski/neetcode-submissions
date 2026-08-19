class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        for x in s:
            if x in hash:
                hash[x] += 1
            else:
                hash[x] = 1

        hash2 = {}
        for x in t:
            if x in hash2:
                hash2[x] += 1
            else:
                hash2[x] = 1
        
        if hash == hash2:
            return True

        return False