class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        t = [[-1 for _ in range(n)] for _ in range(m)]

        def solve(i, j):
            if i >= m or j >= n:
                return 0
            if matrix[i][j] == 0:
                return 0
            if t[i][j] != -1:
                return t[i][j]

            right = solve(i, j + 1)
            diagonal = solve(i + 1, j + 1)
            below = solve(i + 1, j)

            t[i][j] = 1 + min(right, diagonal, below)
            return t[i][j]

        result = 0
        for i in range(m):
            for j in range(n):
                result += solve(i, j)

        return result