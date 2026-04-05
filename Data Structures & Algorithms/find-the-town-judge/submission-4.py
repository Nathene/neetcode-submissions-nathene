class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        inbound, outbound = [0] * (n+1), [0] * (n+1)

        for i, o in trust:
            inbound[i] += 1
            outbound[o] += 1
        
        for i in range(n+1):
            if inbound[i] == 0 and outbound[i] == n - 1:
                return i
        
        return -1