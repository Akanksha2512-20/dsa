# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root,path):
            if not root:
                return
            if not root.left and not root.right:
                path += str(root.val)
                res.append(path)
                return
                
            path += str(root.val) + "->"   
            dfs(root.left,path)
            dfs(root.right,path)
        dfs(root,"")    
        return res

        