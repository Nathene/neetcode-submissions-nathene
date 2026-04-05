class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        best = r

        def can_eat(k: int) -> bool:
            time = 0
            for b in piles:
                time += math.ceil(b / k)
                if time > h:
                    return False
            
            return True

            
        while l < r:
            m = (l + r) // 2
            if can_eat(m):
                best = min(best, m)
                r = m 
            else:
                l = m + 1
        
        return best