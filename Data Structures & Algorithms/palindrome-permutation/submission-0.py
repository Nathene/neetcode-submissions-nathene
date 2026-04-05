class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = Counter(s)


        one = False

        for val in count.values():
            if val % 2 == 1:
                if one: return False
                else: one = True
        
        return True
            