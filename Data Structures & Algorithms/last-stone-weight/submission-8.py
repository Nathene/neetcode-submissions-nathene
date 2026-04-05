class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)

        while heap:
            if len(heap) == 1:
                return abs(heap[0])
            
            s1, s2 = heapq.heappop(heap), heapq.heappop(heap)

            if s1 == s2:
                continue
            
            new_max = abs(s1 - s2)
            heapq.heappush(heap, -new_max)
        
        return 0

            
