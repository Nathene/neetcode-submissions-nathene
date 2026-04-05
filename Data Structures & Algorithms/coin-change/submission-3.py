from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def solve(rem: int) -> int:
            if rem < 0: return float('inf')
            if rem == 0: return 0
            
            res = float('inf')
            for coin in coins:
                sub_res = solve(rem - coin)
                if sub_res != float('inf'):
                    res = min(res, sub_res + 1)
            
            return res
        
        ans = solve(amount)
        return ans if ans != float('inf') else -1