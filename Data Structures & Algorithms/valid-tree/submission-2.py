class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree if every node is coonnected and there are no loops
        Map = {i: [] for i in range(n)}
        for a, b in edges:
            Map[a].append(b)
            Map[b].append(a)

        visited = set()

        def dfs(curr, parent):
            if curr in visited:
                return False
            visited.add(curr)

            for b in Map[curr]:
                if b != parent:
                    if not dfs(b, curr):
                        return False
                        
            return True
        
        # loops
        if not dfs(0, -1):
            return False
        # if all visited
        if len(visited) != n:
            return False
        return True

        


