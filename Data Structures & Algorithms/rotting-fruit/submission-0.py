class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return
        rows, cols = len(grid), len(grid[0])

        L = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    L.append((r,c))
        minute = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while L:
            new_L = []
            last_found = 0
            for r,c in L:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        new_L.append((nr,nc))
                        last_found += 1
            if last_found >= 1:
                minute += 1
            L = new_L
            


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minute
        