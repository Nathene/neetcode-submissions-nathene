class Solution:
    def scoreOfString(self, s: str) -> int:
        rolling_sum = 0

        for i in range(len(s) - 1):
            if ord(s[i]) > ord(s[i + 1]):
                rolling_sum += ord(s[i]) - ord(s[i + 1])
            else:
                rolling_sum += ord(s[i+1]) - ord(s[i])
        
        return rolling_sum