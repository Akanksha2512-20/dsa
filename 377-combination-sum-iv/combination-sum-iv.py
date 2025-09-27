class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {0:1}
        def dfs(target):
            if target in memo:
                return memo[target]
            if target==0:
                return 1
               
            count = 0
            for i in range(len(nums)):
                if target-nums[i]>=0:
                    count =count + dfs(target-nums[i]) 
            memo[target]= count        
            return count        
         
        return dfs(target)