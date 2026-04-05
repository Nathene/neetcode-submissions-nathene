"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def all_same(n: int, r: int, c: int) -> bool:
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        return False
            
            return True

        def dfs(n: int, r: int , c: int) -> 'Node':
            """Recursively constructs a QuadTree from a grid section.

            Args:
                n: The side length of the current square grid section.
                r: The starting row index of the current section.
                c: The starting column index of the current section.

            Returns:
                A Node representing the root of the constructed QuadTree 
                for this section.
            """
            # Base case: A 1x1 grid is always a leaf
            if n == 1:
                return Node(grid[r][c], True)
            
            half = n // 2
            # 1. Divide and Conquer (Go deep first)
            top_left = dfs(half, r, c)
            top_right = dfs(half, r, c + half)
            bottom_left = dfs(half, r + half, c)
            bottom_right = dfs(half, r + half, c + half)

            # 2. Compare the children (The "Aha!" moment)
            # If all 4 children are leaves and have the same value, 
            # merge them into a single leaf.
            if (top_left.isLeaf and top_right.isLeaf and 
                bottom_left.isLeaf and bottom_right.isLeaf and
                top_left.val == top_right.val == bottom_left.val == bottom_right.val):
                return Node(top_left.val, True)

            # 3. Otherwise, return a parent node
            return Node(0, False, top_left, top_right, bottom_left, bottom_right)


        return dfs(len(grid), 0, 0)