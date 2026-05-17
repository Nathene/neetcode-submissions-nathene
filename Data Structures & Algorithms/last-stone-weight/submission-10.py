class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        heap = [-x for x in stones]
        
        heapq.heapify(heap)

        while len(heap) > 1:
            a, b = -heapq.heappop(heap), -heapq.heappop(heap)

            if a != b:
                new_stone = abs(a - b)
                heapq.heappush(heap, -new_stone)
        
        return -heap[0] if len(heap) > 0 else 0



