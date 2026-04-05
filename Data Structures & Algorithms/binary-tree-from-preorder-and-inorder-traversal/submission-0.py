# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(pre, ino):
            if not pre or not ino:
                return None
            root = TreeNode(pre[0])
            idx = ino.index(pre[0])
            root.left = helper(pre[1: idx + 1], ino[:idx])
            root.right = helper(pre[idx + 1:], ino[idx + 1:])

            return root

        return helper(preorder, inorder)