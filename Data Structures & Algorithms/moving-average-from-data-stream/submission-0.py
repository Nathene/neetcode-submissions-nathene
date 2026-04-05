class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.curr_sum = 0
        self.size = 0
        self.cap = size

    def next(self, val: int) -> float:
        if self.size >= self.cap:
            self.size -= 1
            old_val = self.q.popleft()
            self.curr_sum -= old_val
        self.size += 1
        self.curr_sum += val
        self.q.append(val)
        return self.curr_sum / self.size
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
