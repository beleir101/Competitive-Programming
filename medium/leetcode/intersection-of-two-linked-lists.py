# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        la = 0
        lb = 0
        currA = headA
        while currA:
            tail = currA
            currA = currA.next
            la += 1
        currB = headB
        while currB:
            tailB = currB
            currB = currB.next
            lb += 1
        if tailB != tail:
            return None
        currA = headA
        currB = headB
        while la > lb:
            lb += 1
            currA = currA.next
        while lb > la:
            la += 1
            currB = currB.next
        while currB and currA:
            if currB == currA:
                return currA
            currB = currB.next
            currA = currA.next
        return None