class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = { order[i]: i for i in range(26) }
        
        for i in range(len(words) - 1):
            # compare two different words at a time
            w1, w2 = words[i], words[i+1]
            # loop through the first word, assume its shorter
            for j in range(len(w1)):
                # check to see if actually the second word is shorter
                if j == len(w2):
                    return False
                # if these words have different characters at j, make sure theyre in order.
                if w1[j] != w2[j]:
                    # does b come before a?
                    if mp[w1[j]] > mp[w2[j]]:
                        return False
                    break
        
        return True


