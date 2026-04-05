class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = { 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz" }
        res = []
        def backtrack(i: int, path: str):
            if len(path) == len(digits):
                res.append(path[::])
                return
            if digits[i] == "":
                return
            for digit in digit_map[int(digits[i])]:
                backtrack(i + 1, path + digit)
            
        
        backtrack(0, "")
        return res