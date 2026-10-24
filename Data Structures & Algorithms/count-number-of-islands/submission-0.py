class Solution:

  def numIslands(self, grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
      return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r: int, c: int) -> None:
      # Boundary check and water check
      if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
        return

      # "Sink" the island (marks as visited)
      grid[r][c] = "0"

      # Explore 4 orthogonal directions
      dfs(r + 1, c)
      dfs(r - 1, c)
      dfs(r, c + 1)
      dfs(r, c - 1)

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == "1":
          islands += 1
          dfs(r, c)  # Sinks the entire connected component

    return islands
