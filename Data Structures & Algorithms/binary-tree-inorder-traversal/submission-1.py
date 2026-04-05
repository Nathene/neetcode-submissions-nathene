# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def in_order(node: TreeNode) -> None:
            if not node:
                return
            
            in_order(node.left)
            res.append(node.val)
            in_order(node.right)
        
        in_order(root)
        return res