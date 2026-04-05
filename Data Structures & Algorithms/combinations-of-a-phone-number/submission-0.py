class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = { 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz" }
        res = []
        def backtrack(s: str, path: str):
            if len(path) == len(digits):
                res.append(path[::])
                return
            if s == "":
                return
            for digit in digit_map[int(s[0])]:
                backtrack(s[1:], path + digit)
            
        
        backtrack(digits, "")
        return res