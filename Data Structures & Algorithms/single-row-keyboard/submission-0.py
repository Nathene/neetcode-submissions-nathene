class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        letters = { c:i for i, c in enumerate(keyboard) }

        start = 0
        total = 0
        for i in range(len(word)):
            total += abs(letters[word[i]] - start)
            start = letters[word[i]]

        return total