class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = { "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        if digits == "":
            return res
        def backtrack(start: int, path: str) -> None:
            if len(path) == len(digits):
                res.append(path)
                return
            
            for i in range(start, len(digits)):
                num = digits[i]
                for c in digit_map[num]:
                    backtrack(i + 1, path + c)
            

        

        backtrack(0, "")
        return res