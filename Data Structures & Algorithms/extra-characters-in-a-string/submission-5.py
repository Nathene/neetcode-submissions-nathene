from functools import cache
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        @cache
        def backtrack(i: int, extra: int) -> None:
            if i == len(s):
                return extra
            curr = backtrack(i + 1, extra + 1)

            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in dictionary:
                    curr = min(curr, backtrack(j + 1, extra))

            return curr

        return backtrack(0, 0)


