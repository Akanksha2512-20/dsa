class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num]=1
            else:
                count[num]+=1
        for i in count:
            if count[i]==1:
                return i
            