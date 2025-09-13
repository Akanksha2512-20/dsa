class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        freq = {}
        for num in nums:
            freq[num]= freq.get(num,0)+1
            if freq[num]>count:
                count = freq[num]
                res = num
        return res        

        
        
            

