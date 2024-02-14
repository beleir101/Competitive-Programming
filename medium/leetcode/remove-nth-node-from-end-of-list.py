# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        f,l,r = dummy,0,0
        curr = dummy
        while curr:
            if r-l == n+1:
                f = f.next
            else:
                r += 1
            curr = curr.next
        f.next = f.next.next
        return dummy.next
        
