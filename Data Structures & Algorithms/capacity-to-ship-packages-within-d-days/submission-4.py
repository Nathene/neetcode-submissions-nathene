class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_send(amount: int) -> bool:
            total = 0
            total_days = 1

            for weight in weights:
                if total + weight > amount:
                    total_days += 1
                    total = weight
                else:
                    total += weight
                if total_days > days:
                    return False
            
            return total_days <= days
        
        left, right = max(weights), sum(weights)
        best = 0
        while left <= right:
            mid = (left + right) // 2

            if can_send(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best