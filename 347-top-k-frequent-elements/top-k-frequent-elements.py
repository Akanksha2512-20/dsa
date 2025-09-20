class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]= freq.get(nums[i]) + 1
        arr = []        
        for  key,val in freq.items():
            arr.append([val,key])
        arr.sort()
        res =[]
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

                
        