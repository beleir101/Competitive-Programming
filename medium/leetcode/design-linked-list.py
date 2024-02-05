class MyLinkedList:

    def __init__(self):
        self.end = []
        self.start =[]

    def get(self, index: int) -> int:
        if len(self.start)+len(self.end) <= index:
            return -1
        elif len(self.start)>index:
            return self.start[-1-index]
        else:
            index = index-len(self.start)
            return self.end[index]
    def addAtHead(self, val: int) -> None:
        self.start.append(val)
    def addAtTail(self, val: int) -> None:
        self.end.append(val)
    def addAtIndex(self, index: int, val: int) -> None:
        if len(self.start)+len(self.end) < index:
            return 
        elif len(self.start)>index:
            index = len(self.start)-index
            self.start = self.start[:index]+[val]+self.start[index:]
        else:
            index = index-len(self.start)
            self.end = self.end[:index]+[val]+self.end[index:]
    def deleteAtIndex(self, index: int) -> None:
        if len(self.start)+len(self.end) <= index:
            return 
        elif len(self.start)>index:
            index = len(self.start)-1-index
            self.start = self.start[:index]+self.start[index+1:]
        else:
            index = index-len(self.start)
            self.end = self.end[:index]+self.end[index+1:]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)