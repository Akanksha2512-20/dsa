# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next    
        prev = slow.next = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        first, second = head,prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2
                          