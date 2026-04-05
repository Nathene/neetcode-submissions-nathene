class MyStack:

    def __init__(self):
        self.q = deque()
        self.secondary = deque()
    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        while len(self.q) > 1:
            self.secondary.append(self.q.popleft())
        
        val = self.q.popleft()
        self.q = self.secondary
        self.secondary = deque()
        return val

    def top(self) -> int:
        while len(self.q) > 1:
            self.secondary.append(self.q.popleft())
        
        val = self.q.popleft()
        self.secondary.append(val)
        self.q = self.secondary
        self.secondary = deque()
        
        return val

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()