class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i,current_sum):
            if current_sum == amount:
                return 1
            if current_sum >amount or i == len(coins):
                return 0   
            if (i,current_sum) in memo:
                return memo[(i,current_sum)]    
            res = dfs(i, current_sum + coins[i]) + dfs(i+1,current_sum)

            memo[(i,current_sum)]=res
            return res    
        return dfs(0,0)


        