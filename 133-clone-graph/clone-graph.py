"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
    
        cloned_nodes = {}
        def dfs(node):
            if node in cloned_nodes:
                return cloned_nodes[node]

            clone = Node(node.val)
            cloned_nodes[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        return dfs(node)
        