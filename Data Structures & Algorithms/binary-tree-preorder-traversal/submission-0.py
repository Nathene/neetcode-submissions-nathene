# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def generate(node):
            if node:
                yield node.val
                yield from generate(node.left)
                yield from generate(node.right)
        
        return list(generate(root))