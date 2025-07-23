class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count = 0
        flatten = [c for r in matrix for c in r]
        flatten.sort()                    
        return flatten[k-1] 
        