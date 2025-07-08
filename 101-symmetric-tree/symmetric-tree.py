# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def preorder(p,q):
            if not p and not q:
                return True

            if  not p or  not q or p.val != q.val:
                return False

            a= preorder(p.left,q.right)    
            b= preorder(p.right,q.left)
            if a==b:
                return a
            return False    
        return preorder(root.left,root.right)