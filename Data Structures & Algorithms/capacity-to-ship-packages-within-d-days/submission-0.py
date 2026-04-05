class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_finish(k: int) -> bool:
            days_counted = 1
            curr_load = 0
            for w in weights:
                if curr_load + w > k:
                    days_counted += 1
                    curr_load = 0
                curr_load += w
            return days_counted <= days
        
        left, right = max(weights), sum(weights)
        best_answer = right
        while left <= right:
            mid = left + (right - left) // 2 # dont have to do this in python, as integer overflow doesnt exist
        
            if can_finish(mid):
                best_answer = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best_answer


