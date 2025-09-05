class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = l
        while l <= r:
            k = (l + r)//2
            total = 0
            for p in piles:
                total += math.ceil(float(p)/k)
            if total <= h:
                r = k-1
                res = k
            else:
                l = k + 1
        return res                
