class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
            n = len(edges)
            adj = [[] for _ in range(n + 1)]

            def dfs(node, parent):
                if node in visited:
                    return True
                
                visited.add(node)
                for b in adj[node]:
                    if b == parent:
                        continue
                    if dfs(b, node):
                        return True
                return False



            
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
                visited = set()
                if dfs(a, -1):
                    return [a, b]
            return []



        
        
