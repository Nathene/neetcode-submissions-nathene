class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        return list(self.gen(nums))
    
    def gen(self, heap: list[int]) -> Generator[int, None, None]:
        while heap: yield heapq.heappop(heap)