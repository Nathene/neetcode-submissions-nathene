class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # some sort of topological sort involved.

        # queries, indicate we want to do this efficiently, possibly involving soem hashmap

        # return type is a list of bools reflected by the list of queries
        # kind of thinking union find, but also not.. 
        # intuition -> 
        # create the adj list, for all pre reqs.

        # once we have that adj list, we can then brute force the queries, in a for loop.

        # go through each query, use a helper function and return whether someway down the adj list,
        # there exists the target query.

        # some optimization for the future might be for every start node, have every downstream crs in a set. fft

        adj = defaultdict(list)
        is_pre_req = defaultdict(set) # come back to this later...
        for pre, crs in prerequisites:
            adj[pre].append(crs)
        
        memo = {}
        def find(pre: int, crs: int) -> bool:
            if (pre, crs) in memo:
                return memo[(pre, crs)]
            if pre == crs:
                return True
            res = False
            for nei in adj[pre]:
                if find(nei, crs):
                    res = True
                    break     

            memo[(pre, crs)] = res
            return res

        res = []

        for pre, crs in queries:
            res.append(find(pre, crs))
        
        return res

