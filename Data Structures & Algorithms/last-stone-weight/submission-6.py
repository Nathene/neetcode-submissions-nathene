class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while stones:
            left = heapq.heappop(stones)
            if not stones:
                return abs(left)
            right = heapq.heappop(stones)
            left = -left
            right = -right
            print(f"{left} & {right}")
            if right > left:
                heapq.heappush(stones, -(right - left))
            elif left > right:
                heapq.heappush(stones, -(left - right))
            

        
        return abs(stones[0]) if stones else 0