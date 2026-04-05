class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right = n, n
        res = []
        def backtrack(path: str, open_count: int, closed_count: int):
            if len(path) == n * 2:
                res.append(path)
                return
            
            if open_count < n:
                backtrack(path + "(", open_count + 1, closed_count)
            
            if closed_count < open_count:
                backtrack(path + ")", open_count, closed_count + 1)
            
        
        backtrack("", 0, 0)
        return res

            
