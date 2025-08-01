class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def targetcount(i,current_sum):
            if (i,current_sum) in dp:
                return dp[(i,current_sum)] 
            if len(nums)==i:
                return 1 if current_sum == target else 0   
                 
            add = targetcount(i+1,current_sum+nums[i])  
            sub = targetcount(i+1,current_sum-nums[i])
            dp[(i,current_sum)] = add + sub
            return dp[(i,current_sum)]      
        return targetcount(0,0)    