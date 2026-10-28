class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp ={}
        j = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]]=0
            mp[s[i]]+=1    
            while mp[s[i]]>1:
                mp[s[j]]-=1
                j+=1
               
            max_len = max(max_len,i-j+1)    

        return max_len    