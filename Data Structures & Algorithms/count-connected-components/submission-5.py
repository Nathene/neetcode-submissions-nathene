class UnionFind:
    def __init__(self, n: int):
        self.rank = [0] * n
        self.par = [i for i in range(n)]
        

    def find(self, i: int) -> int:
        if self.par[i] == i:
            return i
        while self.par[i] != i:
            i = self.par[i]
        
        return i
    
    def union(self, p: int, q: int):
        n1, n2 = self.find(p), self.find(q)
        if n1 == n2:
            return False
        else:
            if self.rank[n1] > self.rank[n2]:
                self.rank[n1] += 1
                self.par[n2] = n1
            elif self.rank[n2] > self.rank[n1]:
                self.rank[n2] += 1
                self.par[n1] = n2
            else:
                self.par[n2] = n1
                self.rank[n1] += 1
            
            return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for n1, n2 in edges:
            if uf.union(n1, n2):
                n -= 1
        
        return n 
    


    
            
        

