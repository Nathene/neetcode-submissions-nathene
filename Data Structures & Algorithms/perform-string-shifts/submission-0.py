class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        def switch(word: str, k: int, reverse=0) -> str:
            res = ""
            k %= len(word)
            if not reverse:
                first = word[:k]
                last = word[k:]
                res = last+first
            else:
                first = word[:-k]
                last = word[-k:]
                res = last+first

            return res

        for rev, k in shift:
            s = switch(s, k, rev)
        
        return s