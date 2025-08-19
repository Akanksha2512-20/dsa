# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reversek(head,k):
            prev = None
            cur= head
            while k>0:
                next_node = cur.next
                cur.next=prev
                prev= cur
                cur=next_node
                k-=1
            return prev    
        cur = head
        count =  0 
        while cur and count < k:
            cur = cur.next
            count +=1
            if count == k:
                reverse_head = reversek(head,k)
                head.next = self.reverseKGroup(cur, k)
                return reverse_head
        return head        

                
        