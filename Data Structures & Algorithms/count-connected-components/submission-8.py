class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for src, dst in edges:
            if uf.union(src, dst):
                n -= 1        
    
        return n
        


class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [0] * n 
    
    def find(self, p: int) -> int:
        while self.par[p] != p:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p
    
    def union(self, n1: int, n2: int) -> bool:
        p, q = self.find(n1), self.find(n2)
        if p == q:
            return False
        
        if self.rank[p] > self.rank[q]:
            self.par[q] = p
        elif self.rank[q] > self.rank[p]:
            self.par[p] = q
        else:
            self.par[q] = p
            self.rank[p] += 1
        
        return True