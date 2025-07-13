class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        t_count = Counter(t)
        req = len(t_count)
        left = 0
        formed = 0
        min_len = float('inf')
        min_win = (0,0)
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1

            if s[right] in t_count and t_count[s[right]]==freq[s[right]]:
                formed += 1

            while req==formed and left <= right:
                if right-left + 1 < min_len:
                    min_len = min(min_len,right-left+1)
                    min_win = (left,right)
                freq[s[left]] -=1

                if s[left] in t_count and freq[s[left]]< t_count[s[left]]:
                    formed-=1
                
                left+=1
                
        l, r = min_win
        return s[l:r+1] if min_len!= float('inf') else ""  


        