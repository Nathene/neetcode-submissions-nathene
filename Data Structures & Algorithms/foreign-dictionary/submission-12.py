class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)

        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]
            if len(word2) < len(word1) and word2 == word1[:len(word2)]: return ""
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    break
        print(adj)
        # examples
        """
        "hrn","hrf","er","enn","rfnn"

        [n -> [f]], [h, -> [e]], [e -> [r]], [r -> [n]]

        """
        
        res = []
        visited = set()
        cycle = set()
        def dfs(src: str) -> bool:
            if src in cycle:
                return True
            cycle.add(src)
            
            for nei in adj[src]:
                if nei not in visited:
                    if dfs(nei): return True
            res.append(src)
            cycle.remove(src)
            visited.add(src)

            return False
            
        for word in words:
            for letter in word:
                if letter not in visited:
                    if dfs(letter): return ""

        return "".join(res[::-1])
            














        """
        some assumptions
        almost a union find problem?
        but also not really, as it may be connected, but we dont know the original orderings.
        It is the case the input is sorted
        therefore, given the first index of the words,
        if they differ, it is the case that the ith - 1 word, is lexiographically smaller
        than the ith word. if we are comparing word[i - 1] and word[i]

        It is also the case then, that for any children the smaller letter has
        they are also smaller than the ith - 1 letter
        Quick example. 
        word[i - 1] = "tpr"
        word[i] = "fpr"

        result = "tfpr"

        since, t < f < pr 
        however, it is unknown if p < r or r < p as we dont have enough knowledge.

        proof by contradiction in english:
        "azh"
        "ezhx"
        it IS the case that a < e and it is the case that a < e < z
        however that does not mean it is the case that z < h.
"".join(find(words[0][0]))
        """
