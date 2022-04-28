class MyQueue:

    def __init__(self):
        self.myStack = []
        self.tempStack = []

    def push(self, x: int) -> None:
        for i in range(len(self.myStack)):
            self.tempStack.append(self.myStack.pop())
        self.tempStack.append(x)
        for i in range(len(self.tempStack)):
            self.myStack.append(self.tempStack.pop())
        
    def pop(self) -> int:
        return self.myStack.pop()

    def peek(self) -> int:
        return self.myStack[-1]
        
    def empty(self) -> bool:
        return len(self.myStack) == 0

