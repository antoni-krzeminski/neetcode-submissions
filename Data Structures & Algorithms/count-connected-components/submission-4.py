class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        Map = {i: [] for i in range(n)}
        for a, b in edges:
            Map[a].append(b)
            Map[b].append(a)

        allvisited = set()
        visited = set()
        def dfs(curr):
            allvisited.add(curr)
            if curr in visited:
                return

            visited.add(curr)
            for b in Map[curr]:
                dfs(b)
            visited.remove(curr)

            Map[curr] = []

        ans = 0

        for i in range(n):
            if Map[i] != []:
                ans += 1
                dfs(i)
            
        for i in range(n):
            if i not in allvisited:
                ans += 1

        return ans
            
