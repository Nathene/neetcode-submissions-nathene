class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(list)
        outgoing = defaultdict(list)

        for out, inc in trust:
            incoming[inc].append(out)
            outgoing[out].append(inc)
        
        for i in range(1, n + 1):
            if len(incoming[i]) == n - 1 and len(outgoing[i]) == 0: return i
        
        return -1