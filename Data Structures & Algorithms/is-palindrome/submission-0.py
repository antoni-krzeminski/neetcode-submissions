class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newstr = ''
        for c in s:
            if c.isalnum():
                newstr += c
        if newstr == newstr[::-1]:
            return True
        return False