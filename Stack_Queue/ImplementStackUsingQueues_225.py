import queue

class MyStack:

    def __init__(self):
        self.myQueue = queue.Queue()
        self.tempQueue = queue.Queue()        

    def push(self, x: int) -> None:
        self.myQueue.put(x)
        self.myTop = x        

    def pop(self) -> int:
        print(self.myQueue.qsize())
        for i in range(self.myQueue.qsize()-1):
            item = self.myQueue.get()
            self.tempQueue.put(item)
            self.myTop = item
        result = self.myQueue.get()
        temp = self.myQueue
        self.myQueue = self.tempQueue
        self.tempQueue = temp
        return result                

    def top(self) -> int:
        return self.myTop        

    def empty(self) -> bool:
        return self.myQueue.qsize() == 0
        

