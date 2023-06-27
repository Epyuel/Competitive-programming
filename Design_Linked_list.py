class MyLinkedList:

    def __init__(self):
        self.llst=[]

    def get(self, index: int) -> int:
        if index<len(self.llst):
            return self.llst[index]
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        temp=[val]
        self.llst=temp+self.llst

    def addAtTail(self, val: int) -> None:
        self.llst.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if len(self.llst)>=index:
            temp=[val]
            self.llst=self.llst[:index]+temp+self.llst[index:]
    def deleteAtIndex(self, index: int) -> None:
        if len(self.llst)>index:
            self.llst.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
