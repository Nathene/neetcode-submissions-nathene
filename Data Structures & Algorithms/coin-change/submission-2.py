from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def solve(curr: int) -> float:
            if curr == amount:
                return 0
            if curr > amount:
                return float("inf")
            
            least = float("inf")
            for i in range(len(coins)):
                res = solve(curr + coins[i])
                if res != float("inf"):
                    least = min(least, res + 1)
            
            return least
        
        result = solve(0)
        return result if result != float("inf") else -1