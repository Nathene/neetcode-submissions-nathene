class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_size = max(piles)
        
        l, r = 1, max_size


        while l <= r:
            time = 0
            mid = l + (r - l) // 2

            for b in piles:
                time += math.ceil((b + mid - 1) // mid)
            
            if time > h:
                l = mid + 1
            else:
                r = mid - 1

        return l


