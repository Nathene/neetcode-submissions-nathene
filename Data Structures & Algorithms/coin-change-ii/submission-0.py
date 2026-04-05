class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        def dp(i: int, curr_count: int) -> int:
            if (i, curr_count) in memo:
                return memo[(i, curr_count)]
            if curr_count == amount:
                return 1
            if curr_count > amount or i == len(coins):
                return 0
            add = dp(i, curr_count + coins[i])
            dont_add = dp(i + 1, curr_count)

            memo[(i, curr_count)] = add + dont_add 
            return memo[(i, curr_count)]
        
        return dp(0, 0)