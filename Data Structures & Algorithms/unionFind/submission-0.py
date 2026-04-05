class UnionFind:
    
    def __init__(self, n: int):
        self.size = n
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        n1, n2 = self.find(x), self.find(y)
        if n1 == n2:
            return False
            # already connected
        if self.rank[n1] > self.rank[n2]:
            self.par[n2] = n1
        elif self.rank[n1] < self.rank[n2]:
            self.par[n1] = n2
        else:
            self.par[n2] = n1
            self.rank[n1] += 1
        self.size -= 1
        return True

    def getNumComponents(self) -> int:
        return self.size

