class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pairs = list(zip(gas, cost))

        if sum(gas) < sum(cost): return -1
        res = 0
        curr = 0
        for i in range(len(pairs)):
            curr += pairs[i][0] - pairs[i][1]
            if curr < 0:
                res = i + 1
                curr = 0
                
        
        return res
