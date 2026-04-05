class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        heap = []

        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        
        for i in range(k):
            frq, ele = heapq.heappop(heap)
            res.append(ele)
        
        return res