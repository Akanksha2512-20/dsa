class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2!=0:
            return False
        half = total //2
        dp = {}
        def can_find_subset(i,current):
            if current== half:
                return True
            if current > half or i>= len(nums):
                return False  
            if (i, current) in dp:
                return dp[(i, current)]    
            dp[(i,current)] = (can_find_subset(i + 1, current+ nums[i]) or 
                can_find_subset(i + 1, current))
            return dp[(i,current)]    
        return can_find_subset(0,0)             

        