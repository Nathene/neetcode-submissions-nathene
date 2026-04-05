class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        curr = 0
        res = 0
        i = 0
        for g, c in zip(gas, cost):
            curr += (g - c)
            if curr < 0:
                curr = 0
                res = i + 1
            i += 1

        return res