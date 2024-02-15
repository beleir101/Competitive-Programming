class ListNode:
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.curr = self.head
    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url,self.curr,None)
        self.curr = self.curr.next
    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev is None:
                return self.curr.val
            self.curr = self.curr.prev
        return self.curr.val
    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next is None:
                return self.curr.val
            self.curr = self.curr.next
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)