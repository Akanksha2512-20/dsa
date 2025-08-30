class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        maxf=0
        j=0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1
            maxf = max(maxf,count[s[i]])
            while (i-j + 1)- maxf > k:
                count[s[j]]-=1
                j+=1 
            res = max(res,i-j+1)    
        return res        
                


            
            






        