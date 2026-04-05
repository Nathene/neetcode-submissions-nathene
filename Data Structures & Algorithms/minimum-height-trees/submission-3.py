class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        edge_count = {}
        leaves = deque()
        for src, nei in adj.items():
            if len(nei) == 1:
                leaves.append(src)
            edge_count[src] = len(nei)
        
        while leaves:
            if n <= 2: return list(leaves)
            for i in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for nei in adj[leaf]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves.append(nei)

        return [0]

                
