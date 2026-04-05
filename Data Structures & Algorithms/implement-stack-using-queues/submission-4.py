class MyStack:

    def __init__(self):
        self.q = deque()
    
    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        length = len(self.q)
        for _ in range(length - 1):
            val = self.q.popleft()
            self.q.append(val)
        
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return not self.q