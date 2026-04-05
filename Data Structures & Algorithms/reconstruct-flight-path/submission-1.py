class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        res = []

        adj = defaultdict(list)
        for start, end in sorted(tickets, reverse=True):
            adj[start].append(end)
        
        def dfs(airport: str) -> None:
            while adj[airport]:
                next_stop = adj[airport].pop()
                dfs(next_stop)
            
            res.append(airport)
            
        dfs("JFK")
        return res[::-1]