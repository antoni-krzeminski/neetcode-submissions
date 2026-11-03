class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        Map = {i: [] for i in range(n)}
        for a, b in edges:
            Map[a].append(b)
            Map[b].append(a)

        visited = set()

        def bfs(curr, parent):
            print(curr)
            if curr in visited and curr != parent:
                return False
            visited.add(curr)

            for b in Map[curr]:
                if b != parent:
                    if not bfs(b, curr):
                        return False
                        
            return True
        

        if not bfs(0, -1):

            return False
        if len(visited) != n:
            return False
        return True

        


