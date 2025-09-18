class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(i):
            if i ==n:
                return 1
            if i > n:
                return 0   
            if i in memo:
                return memo[i]    
            count = 0
            count+=dfs(i+1)
            count+=dfs(i+2)
            memo[i]=count
            return count
        return dfs(0)          