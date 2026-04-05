class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(i: int) -> None:
            if len(curr) == k:
                res.append(curr[:])
                return
            
            if i > n:
                return
            
            curr.append(i)
            backtrack(i + 1)

            curr.pop()
            backtrack(i + 1)
        
        backtrack(1)
        return res
            
            

