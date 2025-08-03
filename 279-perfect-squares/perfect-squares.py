class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        def dfs(k):
            if k==0:
                return 0
            min_count = float('inf')
            if k in dp:
                return dp[k]
            i= 1
            while i*i <= k:
                min_count= min(min_count,1+dfs(k-i*i))
                i+=1 
                dp[k]=min_count
            return min_count
        return dfs(n)        
        