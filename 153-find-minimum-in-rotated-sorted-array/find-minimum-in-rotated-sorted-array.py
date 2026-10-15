class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]
        for i in range(1,len(nums)):
            res = min(nums[i],res)
        return res    