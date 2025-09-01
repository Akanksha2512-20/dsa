class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        index_mp = {}
        for i in range(len(numbers)):
            num = target-numbers[i]
            if num in index_mp:
                res.append(index_mp[num])  
                res.append(i+1)
            index_mp[numbers[i]]=i+1
        return res    
            
                    
            
        