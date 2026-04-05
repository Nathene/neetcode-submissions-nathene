class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        i = len(self.stack) - 1
        span = 0
        while i >= 0 and self.stack[i] <= price:
            span += 1
            i -= 1
        
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)