class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = {}
        def dfs(x,y):
            if x < 0 or x >=len(obstacleGrid) or y<0 or y>=len(obstacleGrid[0]) or obstacleGrid[x][y]==1:
                return 0
            if x==len(obstacleGrid)-1 and y ==len(obstacleGrid[0])-1:
                return 1
            if (x,y) in dp:
                return dp[(x,y)]
            dp[(x,y)] = dfs(x+1,y) + dfs(x,y+1) 
            return  dp[(x,y)]  
        return dfs(0,0)
        