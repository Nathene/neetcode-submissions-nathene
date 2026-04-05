class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat(amount: int) -> bool:
            hours = 0
            for p in piles:
                hours += math.ceil((p / amount))
            return hours <= h
        
        left = 1
        right = max(piles)
        best = right
        while left < right:

            mid = (left + right) // 2
            if can_eat(mid):
                best = min(best, mid)
                right = mid
            else:
                left = mid + 1
        
        return best
            