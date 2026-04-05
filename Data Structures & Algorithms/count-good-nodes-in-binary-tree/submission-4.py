# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def find_good(node, curr_max) -> int:
            if not node:
                return 0
            happy = 0
            if node.val >= curr_max:
                happy = 1
            curr_max = max(curr_max, node.val)
            return happy + find_good(node.left, curr_max) + find_good(node.right, curr_max)
        return find_good(root, root.val)
            