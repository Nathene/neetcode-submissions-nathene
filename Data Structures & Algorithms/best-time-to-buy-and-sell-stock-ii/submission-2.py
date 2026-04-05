class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        res = 0
        for p in prices[1:]:
            if low < p:
                res += (p - low)
            low = p
        
        return res