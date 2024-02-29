class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.i = 0
        self.s = k
        self.si = 0
    def enQueue(self, value: int) -> bool:
        if self.si-self.i == self.s:
            return False
        self.q.append(value)
        self.si += 1
        return True
    def deQueue(self) -> bool:
        if self.si-self.i == 0:
            return False
        self.i += 1
        return True
    def Front(self) -> int:
        if self.si-self.i == 0:
            return -1
        return self.q[self.i]
    def Rear(self) -> int:
        if self.si-self.i == 0:
            return -1
        return self.q[self.si-1]
    def isEmpty(self) -> bool:
        return self.si == self.i
    def isFull(self) -> bool:
        return self.si-self.i == self.s


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()