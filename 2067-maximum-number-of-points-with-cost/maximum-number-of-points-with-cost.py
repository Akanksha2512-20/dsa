class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        dp = points[0]
        
        for r in range(1, rows):
            left = [0] * cols
            right = [0] * cols
            new_dp = [0] * cols
            
            left[0] = dp[0]
            for c in range(1, cols):
                left[c] = max(left[c-1] - 1, dp[c])
            
            right[-1] = dp[-1]
            for c in range(cols-2, -1, -1):
                right[c] = max(right[c+1] - 1, dp[c])
            
            for c in range(cols):
                new_dp[c] = points[r][c] + max(left[c], right[c])
            
            dp = new_dp
        
        return max(dp)
        