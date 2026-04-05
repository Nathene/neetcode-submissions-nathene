class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, curr, path):
            if curr == target:
                res.append(path[:])
                return
            
            if start == len(candidates) or curr > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if curr + candidates[i] > target:
                    break
                
                path.append(candidates[i])

                backtrack(i + 1, curr + candidates[i], path)
                path.pop()
            
        backtrack(0, 0, [])
        return res