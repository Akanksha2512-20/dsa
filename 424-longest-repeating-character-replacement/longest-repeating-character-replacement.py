class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_len = 0
        max_word = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1
            max_word = max(max_word,freq[s[right]])
            if (right - left + 1) - max_word > k:
                freq[s[left]]-=1
                left += 1
            max_len = max(max_len,right-left+1)
        return max_len       

        