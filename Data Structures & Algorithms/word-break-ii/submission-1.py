class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        curr = []
        word_dict = set(wordDict)
        def backtrack(i: int) -> None:
            if i == len(s):
                res.append(" ".join(curr))
                return
            for j in range(i,  len(s)):
                word = s[i:j+1] 
                if word in word_dict:
                    curr.append(word)
                    backtrack(j + 1)
                    curr.pop()
                
        backtrack(0)
        return res


            

                