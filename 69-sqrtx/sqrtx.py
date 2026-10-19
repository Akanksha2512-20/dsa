class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        res =0
        l = 1
        r = x
        while l <= r:
            mid = (l + r)//2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                r = mid -1 
            else:
                res = mid
                l = mid + 1    
        return res