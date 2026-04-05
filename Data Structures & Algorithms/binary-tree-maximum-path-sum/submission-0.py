# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # at every node, we check the paths left and right, and go down until we hit a negative number
        # if we hit a negative number and there is still more children, then reset the current count to 0, 
        # and continue down that recursive chain

        # at the end, return the MAX sum found. 
        if not root:
            return 0

        res = [root.val]


        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            res[0] = max(res[0], node.val + left_max + right_max)

            return node.val + max(left_max, right_max)

        dfs(root)
        return res[0]