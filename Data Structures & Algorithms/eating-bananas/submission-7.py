class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_finish(k: int):
            curr = 0

            for b in piles:
                curr += math.ceil(b / k)
            
            return curr <= h

        left, right = 1, max(piles)

        best_answer = right

        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                best_answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best_answer
