class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr: str, open_bracket: int, closing_bracket: int) -> None:
            if len(curr) == n * 2:
                res.append(curr[::])
                return
            
            orig = curr
            if open_bracket > 0:
                curr = curr + "("
                backtrack(curr, open_bracket - 1, closing_bracket)
            if closing_bracket > open_bracket:
                curr = orig + ")"
                backtrack(curr, open_bracket, closing_bracket - 1) 

            
        backtrack("", n, n)
        return res
            
            
