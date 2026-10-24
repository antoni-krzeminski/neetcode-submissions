class Solution:

  def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
    if not heights or not heights[0]:
      return []

    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r: int, c: int, visited: set) -> None:
      visited.add((r, c))

      directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        # Flow UPHILL: neighbor height must be >= current cell height
        if (
            0 <= nr < rows
            and 0 <= nc < cols
            and (nr, nc) not in visited
            and heights[nr][nc] >= heights[r][c]
        ):
          dfs(nr, nc, visited)

    # 1. Run DFS from all boundary cells
    # Top and bottom rows
    for c in range(cols):
      dfs(0, c, pacific)  # Top row -> Pacific
      dfs(rows - 1, c, atlantic)  # Bottom row -> Atlantic

    # Left and right columns
    for r in range(rows):
      dfs(r, 0, pacific)  # Left column -> Pacific
      dfs(r, cols - 1, atlantic)  # Right column -> Atlantic

    # 2. Return intersection of coordinates reached by both oceans
    return list(pacific & atlantic)
