"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        def flatten_tail(curr: 'Node') -> 'Node':
            tail = None
            while curr:
                next_node = curr.next
                if curr.child:
                    child_tail = flatten_tail(curr.child)
                    
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None  

                    if child_tail:
                        child_tail.next = next_node
                    if next_node:
                        next_node.prev = child_tail

                    tail = child_tail  
                    curr = child_tail
                else:
                    tail = curr
                    curr = next_node
            return tail
        
        flatten_tail(head)
        return head