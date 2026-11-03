class Solution:

  def countComponents(self, n: int, edges: list[list[int]]) -> int:
    adj = [[] for _ in range(n)]
    for a, b in edges:
      adj[a].append(b)
      adj[b].append(a)

    visited = set()

    def dfs(curr: int) -> None:
      visited.add(curr)
      for neighbor in adj[curr]:
        if neighbor not in visited:
          dfs(neighbor)

    ans = 0

    for i in range(n):
      if i not in visited:
        ans += 1
        dfs(i)

    return ans
