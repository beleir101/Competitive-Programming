# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current = head
        temp = None
        while current:
            tempo = current.next
            current.next = temp
            temp = current
            current = tempo
        return temp