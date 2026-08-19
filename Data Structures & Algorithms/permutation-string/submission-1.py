class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        S1 = []
        for c in s1:
            S1.append(c)
        S1.sort()
        for i in range(len(s2) - len(s1) +1):
            S2 =[]
            for u in range(len(s1)):
                S2.append(s2[u + i])
            S2.sort()
            print(S1)
            print(S2)
            if S2 == S1:
                return True
        return False