class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j=0
        mf=0
        mp={}
        max_len =0
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] =0
            mp[s[i]]+=1
            mf = max(mp[s[i]],mf)
            while (i-j+1)-mf > k:
                mp[s[j]]-=1
                j +=1
            max_len = max(max_len,i-j+1)  
        return max_len      

