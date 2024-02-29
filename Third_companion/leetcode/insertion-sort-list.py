# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        dummy.next = curr
        curr = curr.next
        dummy.next.next = None
        while curr:
            vt = dummy.next
            prev = dummy
            temp = curr.next
            while vt:
                if vt.val >= curr.val:
                    prev.next = curr
                    curr.next = vt
                    break
                elif vt.next == None:
                    vt.next = curr
                    vt.next.next = None
                    break
                
                else:
                    prev = vt
                    vt = vt.next
            curr = temp
        return dummy.next