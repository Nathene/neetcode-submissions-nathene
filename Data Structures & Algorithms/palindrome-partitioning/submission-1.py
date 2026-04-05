class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(i: int, curr: List[str]) -> None:
            if i == len(s):
                res.append(curr[:])
                return
            
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    curr.append(substring)
                    backtrack(j + 1, curr)
                    curr.pop()
        
        backtrack(0, [])
        return res