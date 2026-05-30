class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        res = []
        
        heap = []

        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        while k > 0:
            key, val = heapq.heappop(heap)
            res.append(val)
            k -= 1
        return res
