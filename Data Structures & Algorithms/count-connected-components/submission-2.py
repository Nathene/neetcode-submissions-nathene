class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[parent[x]])
            return parent[x]

        def union(x, y):
            x_par, y_par = find(x), find(y)

            if x_par == y_par:
                return False
            
            if rank[x_par] > rank[y_par]:
                parent[y_par] = x_par
            elif rank[y_par] > rank[x_par]:
                parent[x_par] = y_par
            else:
                parent[y_par] = x_par
                rank[x_par] += 1

            return True


        for p, c in edges:
            union(p, c)
        
        res = set()

        for i in range(n):
            res.add(find(i))
            

        
        return len(res)
