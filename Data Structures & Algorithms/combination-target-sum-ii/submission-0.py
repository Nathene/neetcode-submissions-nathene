class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        candidates.sort()
        def backtrack(i: int, rem: int) -> None:
            if rem == 0:
                res.append(curr[::])
            if rem < 0 or i == len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if candidates[j] == candidates[j-1] and j > i:
                    continue
                curr.append(candidates[j])
                backtrack(j+1, rem - candidates[j])
                curr.pop()


            

        
        backtrack(0, target)
        return res
    