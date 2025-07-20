class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums,target):
            start,end = 0, len(nums)-1
            while start <=end:
                mid = (start + end)//2
                if nums[mid]>=target:
                    end = mid -1
                else:
                    start = mid + 1   
            if start < len(nums) and nums[start]==target:
                return start
            return -1

        def second(nums,target):
            start, end = 0, len(nums)-1
            while start<=end:
                mid = (start + end)//2
                if nums[mid]<=target:
                    start = mid + 1
                else:
                    end = mid -1    
            if end>=0 and nums[end] == target:
                return  end
            return -1   

        return [first(nums,target),second(nums,target)]          