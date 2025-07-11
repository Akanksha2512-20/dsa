# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = [float('inf')]
        prev = [None]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if prev[0] is not None:
                min_diff[0] = min(min_diff[0],root.val-prev[0]) 
            prev[0]=root.val
            dfs(root.right)   

        dfs(root)
    
        return min_diff[0]
        