class Graph:
    
    def __init__(self):
        self.adj = {} # src -> set()

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = set()
        if dst not in self.adj:
            self.adj[dst] = set()
        
        self.adj[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj:
            return False
        
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        return self.dfs(src, dst, set())

    def dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True
        
        visited.add(src)
        for nei in self.adj.get(src, []):
            if nei not in visited:
                if self.dfs(nei, dst, visited): return True
        
        return False


