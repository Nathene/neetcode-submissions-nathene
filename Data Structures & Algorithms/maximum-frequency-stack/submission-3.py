class FreqStack:

    def __init__(self):
        self.items = defaultdict(list)
        self.count = defaultdict(int)
        self.max_count = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        self.items[self.count[val]].append(val)
        self.max_count = max(self.max_count, self.count[val])

    def pop(self) -> int:
        mc = self.max_count
        val = self.items[mc].pop()
        if not self.items[mc]: self.max_count -= 1
        self.count[val] -= 1
        return val
        

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()