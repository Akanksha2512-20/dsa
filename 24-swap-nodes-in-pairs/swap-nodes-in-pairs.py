# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        
        while curr.next and curr.next.next:
            future = curr.next.next
            prev = curr.next
            

            prev.next = future.next
            future.next = prev
            curr.next = future

            curr = prev  
        return dummy.next    

            
        