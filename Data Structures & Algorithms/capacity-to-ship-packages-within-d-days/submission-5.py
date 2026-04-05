class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def can_send(amount: int) -> bool:
            total = 0
            total_days = 1
            for w in weights:
                if total + w > amount:
                    total_days += 1
                    total = w
                else:
                    total += w
            return total_days <= days
                
        best = 0
        while l <= r:
            m = (l + r) // 2
            if can_send(m):
                best = m
                r = m - 1
            else:
                l = m + 1
        
        return best