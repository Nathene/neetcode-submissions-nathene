class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c:set() for w in words for c in w }
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1] 
            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2): # e.g. app -> apple
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {} # will be True -> Seen in the current path. False -> Seen previously
        res = []
        def dfs(some_char: str) -> bool:
            if some_char in visit:
                return visit[some_char]
            visit[some_char] = True

            for nxt_word in adj[some_char]:
                if dfs(nxt_word): return ""
            
            visit[some_char] = False
            res.append(some_char)
   
        
        for c in adj:
            if dfs(c): return ""
        
        return "".join(res[::-1])
            
        