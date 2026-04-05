class Solution:
    def longestPalindrome(self, s: str) -> str:
        # brute force would be to start at the ends of the string, 
        # and check every single combination, which would be O(N^2) time

        # we can use some DP to calculate this a bit faster
        # at every index, check toward and before it
        # for odd and even, and keep track of the biggest word
        longest = s[0] if s else ""
        def solve(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        for i in range(len(s)):
            even = solve(i, i + 1)
            odd = solve(i, i)
            longest = max(longest, even, odd, key=len)
        
        return longest


