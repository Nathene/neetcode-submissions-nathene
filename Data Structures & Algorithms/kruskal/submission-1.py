class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, p: int) -> int:
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]] # inverse ackerman 
            p = self.par[p]
        return p
    
    def union(self, n1: int, n2: int) -> bool:
        p, q = self.find(n1), self.find(n2)
        if p == q:
            return False
        
        if self.rank[p] > self.rank[q]:
            self.rank[p] += self.rank[q]
            self.par[q] = p
        elif self.rank[q] > self.rank[p]:
            self.rank[q] += self.rank[p]
            self.par[p] = q
        else:
            self.par[p] = q
            self.rank[p] += 1

        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        heap = []
        for src, dst, wei in edges:
            heapq.heappush(heap, (wei, src, dst))
        
        total = 0
        components = n
        while heap and components > 1:
            wei, src, dst = heapq.heappop(heap)
            if uf.union(src, dst):
                total += wei
                components -= 1

        if components != 1:
            return -1

        return total
        






