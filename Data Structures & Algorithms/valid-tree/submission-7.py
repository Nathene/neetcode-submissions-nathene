# Given n nodes labeled from 0 to n - 1 and a list of undirected edges 

# (each edge is a pair of nodes), write a function to check whether these 

# edges make up a valid tree.
# what is a valid tree
# graph without cycles

# have some visit set, and make sure we dont visit the same node twice ?
# since its undirected we cant use a topological sort for this, just a normal hashset would work
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
# a valid tree means that the graph is conencted.. 

class UnionFind:
    def __init__(self, size: int):
        self.size = size
        self.par = [i for i in range(size)]
        self.rank = [0] * size
        self.max_nodes = size - 1
        self.nodes = 0
    
    def find(self, p: int) -> int:
        while self.par[p] != p:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return self.par[p]
    
    def union(self, p: int, q: int) -> bool:
        n1, n2 = self.find(p), self.find(q)
        if n1 == n2:
            return False
        
        if self.rank[n1] > self.rank[n2]:
            self.par[n2] = n1
        elif self.par[n2] > self.par[n1]:
            self.par[n1] = n2
        else:
            self.par[n2] = n1
            self.rank[n1] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = UnionFind(n)

        for src, dst in edges:
            if not uf.union(src, dst): return False
        
        return True
    
