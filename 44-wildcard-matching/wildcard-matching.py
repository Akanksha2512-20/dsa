class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def backtrack(s_idx, p_idx):
            if s_idx == len(s) and p_idx == len(p):
                return True
            
            if p_idx == len(p):
                return s_idx == len(s)
            if (s_idx,p_idx) in memo:
                return memo[(s_idx,p_idx)]
            
            if p[p_idx] == '*':
                memo[(s_idx,p_idx)] = (backtrack(s_idx, p_idx + 1) or
                        (s_idx < len(s) and backtrack(s_idx + 1, p_idx)))
            else:
                if s_idx < len(s) and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                    memo[(s_idx,p_idx)]= backtrack(s_idx + 1, p_idx + 1) 
                else:
                    memo[(s_idx, p_idx)] = False               
            
            return memo[(s_idx,p_idx)]
        
        return backtrack(0, 0)
        