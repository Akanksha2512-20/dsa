class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def helper(i, j):
            if i == len(triangle) - 1:
                return triangle[i][j]
            if (i,j) in dp:
                return dp[(i,j)]
            left_path = helper(i + 1, j)
            right_path = helper(i + 1, j + 1)
            dp[(i,j)] = triangle[i][j] + min(left_path, right_path)
            
            return dp[(i,j)]
        
        return helper(0, 0)