# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length+=1
            curr= curr.next
        dummy = ListNode(0,head)    
        curr = dummy
        length = length -n 
        while length >0:
            curr = curr.next
            length = length - 1
        curr.next = curr.next.next
        return dummy.next   



        