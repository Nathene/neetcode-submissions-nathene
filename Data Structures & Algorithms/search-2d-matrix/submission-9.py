class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the correct row
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows - 1
        while l <= r:
            m = (r + l) // 2
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        
        row = r
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        
        return False



        # find the correct col and do a standard binary search.