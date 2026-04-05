class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat(b: int) -> bool:
            curr_pile = 0
            for banana in piles:
                curr_pile += math.ceil(banana / b)
            
            return curr_pile <= h
        
        left, right = 1, max(piles)
        best = 0
        while left <= right:
            mid = (left + right) // 2

            if can_eat(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best
