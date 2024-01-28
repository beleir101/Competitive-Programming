# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        ak = []
        current = head
        while current:
            ak.append(current)
            current = current.next
        if len(ak)%2 == 0:
            return ak[int(len(ak)/2)]
        else:
            return ak[int(((len(ak)+1)/2)-1)]