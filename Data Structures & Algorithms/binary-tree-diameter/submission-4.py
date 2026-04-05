# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        self.total = 0
        @cache
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.total = max(self.total, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.total