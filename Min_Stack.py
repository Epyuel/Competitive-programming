class MinStack:
    def __init__(self):
        self.stack=[]   
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        return

    def pop(self) -> None:
        self.stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        sorted_stack=sorted(self.stack)
        return sorted_stack[0]
