class Solution:
    def reverseBetween(self, head, left, right):
        if head is None:
            return None
        elif head.next is None or left == right:
            return head
        current = head
        count = 1
        st = None
        first = None
        temp = None
        last = None
        ext = None
        while current and count <= right+1:
            if count == left - 1:
                first = current
                current = current.next
            elif left <= count <= right:
                cd = current.next
                if count == left:
                    st = current
                elif count == right:
                    last = current
                current.next = temp
                temp = current
                current = cd
            elif count == right+1:
                ext = current
            else:
                current = current.next
            count += 1
        if left != 1:
            first.next = last
        elif left == 1:
            head = last
        st.next = ext
        return head