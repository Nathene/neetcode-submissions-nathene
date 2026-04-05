class UnionFind:
    def __init__(self, k):
        self.par = [i for i in range(k)]
        self.rank = [0] * k
    
    def find(self, p: int) -> int:
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]] # <- path compression, making sure our "tree" of parents, gets shrunk every time we find a parent. 
            p = self.par[p]                     # this allows for a time complexitry upgrade to  N * inverse ackerman(N) where N == size of the nodes which is almost constant.
        return p
    
    def union(self, n1, n2) -> bool:
        p, q = self.find(n1), self.find(n2)

        if p == q:
            return True
        
        if self.rank[p] > self.rank[q]:
            self.par[q] = p
            self.rank[p] += self.rank[q]
        else:
            self.par[q] = p
            self.rank[p] += self.rank[q]
        
        return True
        


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # somehow have to differentiate between two people with the same name
        uf = UnionFind(len(accounts))
        email_to_account = {} # email to index
        for i, account in enumerate(accounts):
            for emails in account[1:]:
                if emails in email_to_account:
                    uf.union(i, email_to_account[emails])
                else:
                    email_to_account[emails] = i
        
        email_groups = defaultdict(list) # index to emails
        for email, index in email_to_account.items():
            leader = uf.find(index)
            email_groups[leader].append(email)
        
        res = []
        for index, emails in email_groups.items():
            group = [accounts[index][0]]
            group.extend(emails)
            res.append(group)
        
        return res


