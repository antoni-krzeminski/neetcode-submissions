class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        possible = [0] * n
        possible[0] = 1

        for i, num in enumerate(s):
            if possible[i] == 0 or s[i] == '1':
                continue
            for jump in range(minJump, maxJump + 1):
                if i + jump < n:
                    possible[i + jump] = 1
        return True if possible[-1] == 1 and s[-1] == "0" else False