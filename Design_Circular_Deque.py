class MyCircularDeque:

    def __init__(self, k: int):
        self.len=k
        self.deque=[]
        for i in range(self.len):
            self.deque.append(None)
        

    def insertFront(self, value: int) -> bool:
        if not(self.isFull()):
            for i in range(self.len-1,-1,-1):
                self.deque[i]=self.deque[i-1]
            self.deque[0]=value
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if not(self.isFull()):
            for i in range(self.len):
                if self.deque[i]==None:
                    self.deque[i]=value
                    return True
        else:
            return False


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            for i in range(self.len-1):
                self.deque[i]=self.deque[i+1]
            self.deque[-1]=None
            return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.isFull():
                self.deque[-1]=None
                return True
            else:
                for i in range(self.len-1):
                    if self.deque[i+1]==None:
                        self.deque[i]=None
                        return True
                

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            if self.isFull():
                return self.deque[-1]
            else:
                for i in range(self.len-1):
                    if self.deque[i+1]==None:
                        return self.deque[i]


    def isEmpty(self) -> bool:
        for i in self.deque:
            if i!=None:
                return False
        return True

    def isFull(self) -> bool:
        for i in range(self.len):
            if self.deque[i]==None:
                return False
        return True
