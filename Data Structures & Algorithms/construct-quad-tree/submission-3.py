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
            # if the size of the square is 1, return a new Node which ia obviously a leaf.
            if n == 1:
                return Node(grid[r][c], True)
            
            n //= 2
            top_left = dfs(n, r, c)
            top_right = dfs(n, r, c + n)
            bottom_left = dfs(n, r + n, c)
            bottom_right = dfs(n, r + n, c + n)

            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and \
                top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                return Node(top_left.val, True)
            
            return Node(grid[r][c], False, top_left, top_right, bottom_left, bottom_right)


        return dfs(len(grid), 0, 0)