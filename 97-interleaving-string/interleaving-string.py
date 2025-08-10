class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}    
        def dfs(i,j,k):
            if len(s3)==k:
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            valid = False

            if i<len(s1) and s1[i]==s3[k]:
                valid=dfs(i+1,j,k+1)

            if j<len(s2) and s2[j]==s3[k]:
                valid = valid or dfs(i,j+1,k+1)
            memo[(i, j)] = valid
            return valid    
        return dfs(0,0,0)    
