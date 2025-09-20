class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res= 0
        for num in seen:
            if num-1 not  in seen:
                length = 1
                while (num + length)in seen:
                    length +=1
                res = max(res, length) 
        return res           

