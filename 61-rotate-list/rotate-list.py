# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        length = 1
        tail = head 
        while tail.next:
            length+=1
            tail = tail.next
        k = k % length 
        if k == 0:
            return head
        k = length - k
        curr = head
        while k-1:
            curr = curr.next
            k -=1
        
        new_head =curr.next 
        curr.next = None
        tail.next = head
        return new_head 



        