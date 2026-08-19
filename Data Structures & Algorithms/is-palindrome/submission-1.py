class Solution:

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for letter in s:
            if self.alphaNum(letter):
                s2 += letter.lower()


        l = 0
        r = len(s2) - 1
        
        for i in range(len(s2) // 2):
            if s2[l] != s2[r]:
                return False
            l += 1
            r -= 1
        return True