# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node: TreeNode, robbed: bool) -> int:
            if not node:
                return 0
            res = 0
            if not robbed:
                rob_this_node = node.val + dfs(node.left, True) + dfs(node.right, True)
                res = max(res, rob_this_node)
            
            not_rob = dfs(node.left, False) + dfs(node.right, False)

            res = max(res, not_rob)

            return res
        
        return dfs(root, False)
            
