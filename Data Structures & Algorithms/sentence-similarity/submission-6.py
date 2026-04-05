class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        similar = {}

        for key, val in similarPairs:
            if key in similar:
                similar[key].add(val)
            else:
                similar[key] = set()
                similar[key].add(val)
        
        print(similar)
        if len(sentence1) != len(sentence2): return False

        for s1, s2 in zip(sentence1, sentence2):
            print("hi")
            if s1 == s2: continue
            if s1 in similar and s2 in similar[s1]:
                continue
            if s2 in similar and s1 in similar[s2]:
                continue
            
            return False

        return True