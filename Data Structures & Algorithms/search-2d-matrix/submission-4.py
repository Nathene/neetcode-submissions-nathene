class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,  r = 0, len(matrix) -1
        trg_row = 0
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] <= target:
                trg_row = max(trg_row, m)
                l = m + 1

                
        
        l, r = 0, len(matrix[0]) - 1
    
        while l <= r:
            mid = (l + r) // 2
            if matrix[trg_row][mid] > target:
                r = mid - 1
            elif matrix[trg_row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False