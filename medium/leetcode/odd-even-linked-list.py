# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp = head.next
        tail = temp
        curr = head
        i = 1
        while curr:
            if not tail or not curr:
                break
            if i%2:
                curr.next = tail.next
                if curr.next is None:
                    curr.next = temp
                    break
                curr = curr.next
            else:
                tail.next = curr.next
                if tail.next is None:
                    curr.next = temp
                    break
                tail = tail.next
            i += 1
        return head
