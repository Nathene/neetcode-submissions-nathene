class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # what this is asking is, is there some number in this array, where it can be repeated 3 more times? 
        # and we need to use all inputs of this array.
        # match sticks length <= 15, seems to be suboptimal solution expected.
        # some O(2^n) 
        total = sum(matchsticks)
        want = total // 4
        if want * 4 != total:
            return False

        matchsticks.sort(reverse=True)
        buckets = [0] * 4

        def backtrack(i: int) -> bool:
            if i == len(matchsticks):
                return True        

            for j in range(4):
                if buckets[j] + matchsticks[i] <= want:
                    buckets[j] += matchsticks[i]
                    if backtrack(i + 1): return True
                    buckets[j] -= matchsticks[i]
            

            return False


        return backtrack(0)
            



