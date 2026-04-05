class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]
        # get rid of bad triplets:
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            if triplet[0] == target[0]: res[0] = True
            if triplet[1] == target[1]: res[1] = True
            if triplet[2] == target[2]: res[2] = True


        return all(res)
        
        
        