# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.node_list = []
        self.index = -1
        self.inorder(root)

    def inorder(self,root):
        if not root:
            return 
        self.inorder(root.left)
        self.node_list.append(root.val)
        self.inorder(root.right)     
    def next(self) -> int:
        self.index+=1
        return self.node_list[self.index]
        

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.node_list)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()