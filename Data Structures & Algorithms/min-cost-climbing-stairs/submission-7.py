class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if len(cost) < 3:
            return min(cost)
        
        one, two = cost[-1], cost[-2]
        
        for i in range(len(cost) - 3, -1, -1):
            new_val = cost[i] + min(one, two)
            one = two
            two = new_val
        
        return min(one, two)
        

            
       