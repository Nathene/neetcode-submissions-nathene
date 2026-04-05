# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def pre_order(node: TreeNode) -> None:
            if not node:
                return
            
            res.append(node.val)
            pre_order(node.left)
            pre_order(node.right)
        
        pre_order(root)
        return res