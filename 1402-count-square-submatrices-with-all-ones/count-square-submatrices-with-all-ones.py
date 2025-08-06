class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        t = [[0 for _ in range(n+1)] for _ in range(m+1)]

        result = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if matrix[i][j]==1:
                    t[i][j]= 1 + min(t[i+1][j],t[i][j+1],t[i+1][j+1])
                    result+=t[i][j]
        return result