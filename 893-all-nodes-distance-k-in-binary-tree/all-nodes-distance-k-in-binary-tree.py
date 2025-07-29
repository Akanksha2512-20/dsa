# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_map = {}
    
        # Helper function to populate parent_map
        def populate_parents(node, parent=None):
            if node:
                parent_map[node] = parent
                populate_parents(node.left, node)
                populate_parents(node.right, node)

        # Perform BFS to populate parent_map
        populate_parents(root)
        
        # List to store result nodes at distance K
        result = []
        # Set to store visited nodes to prevent cycles
        visited = set()

        # DFS function to find nodes at distance K
        def dfs(node, distance):
            if node is None or node in visited:
                return
            
            visited.add(node)
            
            # If distance is zero, append the current node value to result
            if distance == k:
                result.append(node.val)
                return
            
            # Move to the left child, right child, or the parent node
            if node.left: dfs(node.left, distance + 1)
            if node.right: dfs(node.right, distance + 1)
            if node in parent_map and parent_map[node]: dfs(parent_map[node], distance + 1)

        # Start DFS from the target node
        dfs(target, 0)
        
        return result
        