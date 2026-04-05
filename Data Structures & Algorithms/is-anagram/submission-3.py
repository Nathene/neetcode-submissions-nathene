class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # otherwise
        # count the letters in a map
        # loop through the keys, make sure the values are the same