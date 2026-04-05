from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        visit = set()
        if endWord not in wordList or beginWord == endWord:
            return 0

        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                option = word[:i] + "*" + word[i+1:]
                adj[option].append(word)


        q = deque([(beginWord, 1)]) # [curr_word]
        while q:
            
            curr_word, level = q.popleft()
            print(curr_word, level)
            if curr_word == endWord:
                return level
            
            for i in range(len(curr_word)):
                option = curr_word[:i] + "*" + curr_word[i+1:]
                for opt in adj[option]:
                    if opt not in visit:
                        visit.add(opt)
                        q.append([opt, level + 1])


        
        return 0



