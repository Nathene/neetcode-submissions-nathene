class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        count = defaultdict(int)

        for inbound, outbound in trust:
            adj[inbound].append(outbound)
            count[outbound] += 1
        

        for i in range(1, n+1):
            if adj[i] == [] and count[i] == n-1:
                return i
            
        
        return -1