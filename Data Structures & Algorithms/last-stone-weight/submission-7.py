class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while stones:
            left = abs(heapq.heappop(stones))
            if not stones:
                return abs(left)
            right = abs(heapq.heappop(stones))
            if right > left:
                heapq.heappush(stones, -(right - left))
            elif left > right:
                heapq.heappush(stones, -(left - right))
            

        
        return abs(stones[0]) if stones else 0