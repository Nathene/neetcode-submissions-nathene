class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        memo = {}

        def backtrack(i: int, extra: int) -> None:
            if i == len(s):
                return extra
            if (i, extra) in memo:
                return memo[(i, extra)]
            curr = backtrack(i + 1, extra + 1)

            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in dictionary:
                    curr = min(curr, backtrack(j + 1, extra))

            memo[(i, extra)] = curr
            return curr

        return backtrack(0, 0)


