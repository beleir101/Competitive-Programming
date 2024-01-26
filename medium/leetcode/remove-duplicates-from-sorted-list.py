# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        current = head
        while current:
            temp = current.next
            while temp is not None and temp.val == current.val:
                temp = temp.next                
            current.next = temp
            current = temp
        return head