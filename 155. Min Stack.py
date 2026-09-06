class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if len(self.minStack) == 0:
            self.minStack.append(value)
        else:
            self.minStack.append(min(value, self.minStack[-1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return -1



# Your MinStack object will be instantiated and called as such:

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-1)
minStack.getMin()
minStack.pop()
minStack.getMin()
minStack.pop()
minStack.getMin()
minStack.pop()
minStack.push(-2)
minStack.push(1)
minStack.push(-2)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()
minStack.pop()
minStack.getMin()
minStack.pop()