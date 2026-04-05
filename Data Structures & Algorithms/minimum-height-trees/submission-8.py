class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        visit = set()
       
        def get_farthest(start_node: int) -> list[int, list[str]]:
            q = deque([(start_node, [start_node])])
            visit = set([start_node])
            farthest = start_node
            longest = [start_node]

            while q:
                curr, path = q.popleft()
                if len(path) > len(longest):
                    farthest = curr
                    longest= path
                
                for nei in adj[curr]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, path + [nei]))
            return farthest, longest

        u, _ = get_farthest(0)

        v, path = get_farthest(u)

        mid = len(path) // 2
        if len(path) % 2 == 1:
            return [path[mid]]

        return [path[mid - 1], path[mid]]



            

            
        


        # adj = defaultdict(list)
        # for start, end in edges:
        #     adj[start].append(end)
        #     adj[end].append(start)

        # def bfs(i: int) -> int:
        #     q = deque([(i, 1)])

        #     visit = set()
        #     res = 0
        #     while q:
        #         new_root, level = q.popleft()
        #         visit.add(new_root)
        #         res = level
        #         for nei in adj[new_root]:
        #             if nei not in visit:
        #                 q.append([nei, level + 1])

        #     return res  

        # smallest = n
        # for i in range(n):
        #     smallest = min(smallest, bfs(i))
        # res = []
        # for i in range(n):
        #     if bfs(i) == smallest:
        #         res.append(i)
        
        # return res
        
            
