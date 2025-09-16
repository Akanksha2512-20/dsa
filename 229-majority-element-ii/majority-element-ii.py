class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        n = len(nums)//3
        for num in nums:
            freq[num]= freq.get(num,0)+1
        for key, val in freq.items():
            if val > n:
                res.append(key)
    
        return res           