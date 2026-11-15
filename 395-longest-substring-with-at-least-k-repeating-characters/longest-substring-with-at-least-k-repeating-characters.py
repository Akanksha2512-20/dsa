class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        max_unique = len(set(s))
        for t in range(1,max_unique+1):
            freq=26*[0]
            left = 0
            unique = 0
            at_least_k =0
            for r in range(n):
                r_idx = ord(s[r])-ord('a')
                if freq[r_idx]==0:
                    unique+=1
                freq[r_idx]+=1
                if freq[r_idx]==k:
                    at_least_k +=1

                while unique > t:
                    l_idx = ord(s[left])-ord('a')
                    if freq[l_idx]==k:
                        at_least_k-=1
                    freq[l_idx] -= 1    
                    if freq[l_idx]==0:
                        unique-=1
                    left+=1
                if unique== t and at_least_k==t:
                    max_len =max(max_len, r-left+1)   

        return max_len                     




            