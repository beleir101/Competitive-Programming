# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ls = ListNode(0)
        tail = ls
        grt = ListNode(0)
        gt = grt
        curr = head
        while curr:
            if curr.val < x:
                tail.next = curr
                tail = curr
            else:
                gt.next = curr
                gt = curr
            curr = curr.next
        gt.next = None
        tail.next = grt.next
        return ls.next