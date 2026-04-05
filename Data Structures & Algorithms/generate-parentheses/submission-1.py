class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr: str, open_bracket: int, closing_bracket: int) -> None:
            if len(curr) == n * 2:
                res.append(curr[::])
                return
            
            if open_bracket > 0:
                backtrack(curr + "(", open_bracket - 1, closing_bracket)
            if closing_bracket > open_bracket:
                backtrack(curr + ")", open_bracket, closing_bracket - 1) 

            
        backtrack("", n, n)
        return res
            
            
