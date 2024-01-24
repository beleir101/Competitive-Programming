# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def KindOfReverser(heady):
            if heady is None:
                return head
            current = heady
            temp = None
            lists = []
            while current:
                tempo = current.next
                current.next = temp
                temp = current
                current = tempo
                lists.append(temp.val)
            return temp, lists
        r, k = KindOfReverser(head)
        curry = r
        i = 0
        while curry:
            if curry.val != k[i]:
                return False
            i += 1
            curry = curry.next
        return True