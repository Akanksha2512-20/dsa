class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        visited = set()
        def dfs(i,j):
            if i >= r or i < 0 or j >= c or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            res = dfs(i+1,j)+dfs(i,j+1)+dfs(i-1,j)+dfs(i,j-1)
            return res

        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    return dfs(i, j)
        return 0
