# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def dfs(node: TreeNode) -> None:
            if not node:
                return
            
            cur_max = find_deepest(node.left) + find_deepest(node.right)
            self.best = max(self.best, cur_max)

            dfs(node.left)
            dfs(node.right)

        
        def find_deepest(node: TreeNode) -> int:
            if not node: return 0
            return 1 + max(find_deepest(node.left), find_deepest(node.right))
        
        dfs(root)

        return self.best