class UnionFind:
    def __init__(self, k: int):
        self.count = 0
        self.par = [i for i in range(k)]   
        self.rank = [0] * k

    def find(self, p: int) -> int:
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]] # path comprehension, inverse ackerman
            p = self.par[p]
        return p

    def union(self, p: int, q: int) -> bool:
        p, q = self.find(p), self.find(q)

        if p == q:
            return False
        
        if self.rank[p] > self.rank[q]:
            self.par[q] = p
        elif self.rank[q] > self.rank[p]:
            self.par[p] = q
        else:
            self.par[p] = q
            self.rank[q] += 1
        
        self.count -= 1
        return True
        

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = []
        is_land = [False] * (m * n)
        uf = UnionFind(m * n)
        res = []
        for x, y in positions:
            idx = (x * n) + y
            if is_land[idx]:
                res.append(uf.count)
                continue

            is_land[idx] = True
            uf.count += 1
            
            for nx, ny in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                pos = (nx * n) + ny
                if 0 <= nx < m and 0 <= ny < n and is_land[pos]:
                    uf.union(idx, pos)
            
            res.append(uf.count)
            
        return res
    
    


