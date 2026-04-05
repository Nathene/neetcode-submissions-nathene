class MedianFinder:

    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min heap

    def addNum(self, num: int) -> None:
        if self.small and num > -self.small[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        
        while abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) > len(self.large):
                heapq.heappush(self.large, -heapq.heappop(self.small))
            else:
                heapq.heappush(self.small, -heapq.heappop(self.large))
            


    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 1:
            if len(self.small) > len(self.large):
                return -self.small[0]
            else:
                return self.large[0]
        
        largest = -self.small[0]
        smallest = self.large[0]

        return (largest + smallest) / 2         
        