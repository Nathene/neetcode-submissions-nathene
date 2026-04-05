class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        memo = {}
        dictionary_set = set(dictionary)

        def backtrack(i: int) -> int:
            if i == len(s):
                return 0
            if i in memo:
                return memo[i]
            
            # Option 1: Treat s[i] as an extra character
            res = 1 + backtrack(i + 1)

            # Option 2: Try to find a word starting at index i
            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in dictionary_set:
                    res = min(res, backtrack(j + 1))

            memo[i] = res
            return res

        return backtrack(0)