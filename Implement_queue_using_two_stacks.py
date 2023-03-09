class MyQueue:
    def __init__(self):
        self.stack_1=[]

    def push(self, x: int) -> None:
        self.stack_1.append(x)
        self.stack_2=self.stack_1[::-1]
        return

    def pop(self) -> int:
        poped=self.stack_2.pop()
        self.stack_1=self.stack_2[::-1]
        return poped

    def peek(self) -> int:
        return self.stack_2[len(self.stack_2)-1]

    def empty(self) -> bool:
        if len(self.stack_1)==0:
            return True
        else:
            return False
