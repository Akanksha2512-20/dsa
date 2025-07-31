class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev = 0
        prev2=nums[0]
        for i in range(2,n+1):
            steal = nums[i-1]+prev
            skip = prev2

            temp= max(skip,steal)
            prev = prev2
            prev2 = temp 
        return prev2 

                
