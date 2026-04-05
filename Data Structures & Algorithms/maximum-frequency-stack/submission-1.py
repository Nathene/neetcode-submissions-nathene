class FreqStack:

    def __init__(self):
        self.stack = []
        self.items = defaultdict(list)
        self.count = defaultdict(int)
        self.max_count = 0
    def push(self, val: int) -> None:
        if val in self.count:
            self.count[val] += 1
            self.items[self.count[val]].append(val)
            self.max_count = max(self.max_count, self.count[val])

        else:
            self.count[val] = 1
            self.items[1].append(val)
            self.max_count = max(self.max_count, 1)

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