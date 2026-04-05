class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        potential_word = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                option = word[:i] + "*" + word[i+1:]
                if option not in potential_word:
                    potential_word[option] = []
                potential_word[option].append(word)

        q = deque([(beginWord, 1)])
        seen = set()
        while q:
            
            curr_word, steps = q.popleft()
            
            if curr_word == endWord:
                return steps
            for i in range(len(curr_word)):
                option = curr_word[:i] + "*" + curr_word[i + 1:]

                for opt in potential_word[option]:
                    if opt not in seen:
                        q.append((opt, steps + 1))
                        seen.add(opt)
            

        return 0
        

    