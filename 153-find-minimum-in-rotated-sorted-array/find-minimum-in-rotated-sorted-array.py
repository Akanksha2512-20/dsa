class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = float('inf')
        while l <= r:
            mid = (l + r)//2
            res = min(res,nums[l])
            if nums[l]<=nums[mid]:
                l = mid + 1
            else:
                r = mid 
        return res            
