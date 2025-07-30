class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2  # Start labeling from 2
        island_area = {}  # Map: island_id -> area

        def dfs(r, c, id_):
            if 0 <= r < n and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = id_
                area = 1
                area += dfs(r + 1, c, id_)
                area += dfs(r - 1, c, id_)
                area += dfs(r, c + 1, id_)
                area += dfs(r, c - 1, id_)
                return area
            return 0

        # Step 1: Label islands and store their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area = dfs(r, c, island_id)
                    island_area[island_id] = area
                    island_id += 1

        # Step 2: Try flipping each 0
        max_area = max(island_area.values(), default=0)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                    total = 1 + sum(island_area[id_] for id_ in seen)
                    max_area = max(max_area, total)

        return max_area if max_area > 0 else n * n