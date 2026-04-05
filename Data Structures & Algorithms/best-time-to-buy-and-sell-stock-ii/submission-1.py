class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        low = prices[0]

        for p in prices:
            if low < p:
                res += abs(low - p)
                low = p
            
            low = min(low, p)
        
        return res
