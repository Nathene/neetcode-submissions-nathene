class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)

        return list(self.gen(nums))
    
    def gen(self, heap):
        while heap: yield heapq.heappop(heap)