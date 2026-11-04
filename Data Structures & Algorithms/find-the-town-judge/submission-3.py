class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        maprev = {i: [] for i in range(1, n + 1)}
        map = {i: [] for i in range(1, n + 1)}

        for a, b in trust:
            map[a].append(b)
            maprev[b].append(a)


        for i in range(1, n + 1):
            if len(maprev[i]) == n - 1 and map[i] == []:
                return i

        return -1
