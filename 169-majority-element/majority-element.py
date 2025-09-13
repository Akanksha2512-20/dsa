class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num]= freq.get(num,0)+1
        for key,value in freq.items():
            if value>len(nums)//2:
                return key
        
            

