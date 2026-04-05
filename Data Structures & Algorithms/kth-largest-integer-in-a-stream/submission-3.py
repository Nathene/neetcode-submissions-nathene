import heapq
class KthLargest:


    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        heapq.heapify(nums) # O(N)
        while len(nums) > k:
            heapq.heappop(nums)
        self.k = k
        self.heap = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0] if self.heap else -1

        
