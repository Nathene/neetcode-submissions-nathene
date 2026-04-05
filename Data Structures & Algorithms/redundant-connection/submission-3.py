class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(i: int) -> int:
            while parent[i] != i:
                i = parent[i]
            
            return parent[i]
        
        def union(a: int, b: int) -> bool:
            n1, n2 = find(a), find(b)
            if n1 == n2: return False

            parent[n1] = n2
            return True



        for start, end in edges:
            if not union(start, end):
                return [start, end]
        
        return []