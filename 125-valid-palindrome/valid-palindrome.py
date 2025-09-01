class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        def alnum(c):
            return (ord('A')<=ord(c)<=ord('Z') or ord('a')<=ord(c)<=ord('z') or ord('0')<=ord(c)<=ord('9'))
        while l < r:
            while l < r and not alnum(s[l]):
                l+=1
            while l< r and not alnum(s[r]):
                r-=1    
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1    
        return True        
                
        
        