class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        second = -1
        for i in range(len(nums)):
            if nums[i]==target and first==-1:
                first = i
            if nums[i]==target and first!=-1:
                second = i
        return [first,second]          