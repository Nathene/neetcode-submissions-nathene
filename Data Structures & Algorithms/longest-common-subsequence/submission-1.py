# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def solve(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                return 1 + solve(i + 1, j + 1)

            memo[(i, j)] = max(solve(i + 1, j), solve(i, j + 1))
            return memo[(i, j)]
        
        return solve(0, 0)
                    
            





"""
what do we return when there is no sequence? 

what do we return if text2 is ""?
do we return 0?

can we assume these will always be lowercase chars?
could there be string numbers in here? or characters from UTF8?

can we assume that text2 will always be smaller/bigger than text1? or they could both be the smaller/bigger?

and if i understand the problem correctly, say we have 
t1 = "abcd" and t2 = "hbcd", would we return bcd?

this would be O(n * m) time, as we iterate through the t1 string, t2 amount of times
and the space would be O(1) due to justy returning a string

Refining the Complexity

Next Steps

Before you jump into the code, walk me through your strategy.

How do you plan to track the matches as you move through both strings?

Can you explain why you initially thought O(1) space would work, or if you'd like to revise that to a different data structure?

Would you like to sketch out the high-level logic (or pseudocode) before writing the full Python implementation?

so the brute force of this, would be to iterate through both stirngs, see if the first element appears,
if it does, remember that index for both, and increase the longest sub sequence.

do the same for the next char. Now we have an issue, where we could have the first character of an string, be too late in the array
and that moght cause issue if the remaining k chaarcters are sub sequences before the 0th index. 

To handle this case, we need to keep track of some strings, to make sure, they are indeed contiguous
we can use a map, for each char in the smaller text, that gets assigned the value of the first character in that sub sequence. 
as wwe go forward, if a later character in the array is before an earlier one, we can measure how oong that sub sequence is. 

This would be O(N * M) time, and O(N) memory



Gemini said
I like that you're thinking about the "position" problem—specifically how picking a character too early or too late in the string can block you from finding a longer subsequence later on. That's a classic pitfall in greedy approaches!

However, I want to gently push back on the "contiguous" part of your logic. In this problem, the characters do not need to be next to each other. For example:

text1 = "a1b2c"

text2 = "axbycz"

The LCS is "abc", length 3, even though they are separated by other characters.

Evaluating the Map/Greedy Strategy

Your idea of using a map to track indices is an interesting start, but if you only track the "first" appearance 
or try to build it linearly, you might miss the optimal path. For example, if a character appears multiple times 
in text2, which index do you pick? Picking the first one might be wrong; picking the last one might also be wrong.

To solve this, we usually look at this as a Top-Down (Recursive with Memoization) or Bottom-Up (Tabular) problem.

A Hint on the State

If we compare text1[i] and text2[j]:

If they match: The length of the LCS is 1+LCS of the remaining strings.

If they don't match: The LCS is the better result of either skipping the character in text1 OR skipping the 
character in text2.

Complexity Check

Time: O(n×m) is correct because we need to evaluate the relationship between every character in text1 and every 
character in text2.

Space: With a 2D grid (DP table), it would be O(n×m). Can you think of a way to optimize that to O(min(n,m)) 
since we only ever look at the "previous" results?

How would you structure a 2D array (table) to represent these decisions? What would your "base case" (the values 
for empty strings) look like in that table?

so we would have to either use @cache or a dp[], go through the bigger string, recursivley check if the first char is in both strings,
make a descion to go further in the string to find out, mapping that result in the cache, otherwise, we will also
skip that number and go to the next character in the smaller string. 
carrying that on, like you said previously. The answer would be if text1[i] == text2[j]: LCS = 1 + LCS of text1[i+1] and LCS text[j+1]
"""
