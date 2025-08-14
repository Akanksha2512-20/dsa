class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            y = -x
        else:
            y = x
        reversenum = 0       
        while y:
            last = y % 10
            reversenum = reversenum * 10 + last
            y = y //10
        if reversenum < -2**31 or reversenum > 2**31 - 1:
            return 0    
        return reversenum if x > 0 else -reversenum 



                 
            
        