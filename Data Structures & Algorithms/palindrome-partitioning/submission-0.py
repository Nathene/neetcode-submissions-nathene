from functools import cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # for every character
        # choose to add thaqt character, or not add that character. 
        # if we add that character, is it still a palendrome?
        # if it is? append to result
        # if its not? return

        # Backtracking solution
        # O(N * N^2) time
        # O(N) space 

        res = []
        path = []


        def is_palendrome(word: str) -> bool:
            if not word: return False
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start: int) -> None:
            if start == len(s):
                res.append(list(path))
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palendrome(substring):
                    path.append(substring)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res

        
