class Solution:
    def scoreOfString(self, s: str) -> int:
        rolling_sum = 0

        for i in range(len(s) - 1):
            rolling_sum += abs(ord(s[i]) - ord(s[i + 1]))
        
        return rolling_sum