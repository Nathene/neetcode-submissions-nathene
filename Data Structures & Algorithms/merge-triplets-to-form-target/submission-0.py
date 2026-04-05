class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]
        # get rid of bad triplets:
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            res[0] = max(res[0], triplet[0])
            res[1] = max(res[1], triplet[1])
            res[2] = max(res[2], triplet[2])
        
        return res == target
        
        
        