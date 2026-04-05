class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        mp = {}

        for i, acc in enumerate(accounts):
            for j in range(1, len(acc)):
                email = acc[j]
                if email in mp:
                    uf.union(i, mp[email])
                mp[email] = i

        res_dict = defaultdict(set)
        for i in range(len(accounts)):
            root = uf.find(i)
            for j in range(1, len(accounts[i])):
                res_dict[root].add(accounts[i][j])
        
        ans = []
        for root, emails in res_dict.items():
            ans.append([accounts[root][0]] + sorted(list(emails)))
        return ans
    

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
    
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]

        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        
        return True