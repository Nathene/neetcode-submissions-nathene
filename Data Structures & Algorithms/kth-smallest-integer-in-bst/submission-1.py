# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def generate(node: TreeNode) -> TreeNode:
            if node:
                yield from generate(node.left)
                yield node.val
                yield from generate(node.right)

        gen = generate(root)
        while k > 0:
            res = next(gen)
            k -= 1
        
        return res

    