# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(p, q) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return same(p.left, q.left) and same(p.right, q.right)
        self.flag = False
        def dfs(node):
            if not node:
                return 
            if node.val == subRoot.val:
                if same(node, subRoot):
                    self.flag = True
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.flag

