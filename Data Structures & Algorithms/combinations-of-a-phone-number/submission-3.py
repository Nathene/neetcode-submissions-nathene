class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = { "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz" }
        res = []
        curr = []

        def backtrack(i: int = 0) -> None:
            if len(curr) == len(digits):
                res.append(''.join(curr))
                return
            
            for digit in digit_map[digits[i]]:
                curr.append(digit)
                backtrack(i + 1)
                curr.pop()
        
        backtrack()
        return res