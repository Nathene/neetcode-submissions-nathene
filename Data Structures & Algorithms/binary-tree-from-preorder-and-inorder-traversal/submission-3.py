# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(pre_order, in_order) -> TreeNode:
            if not pre_order or not in_order:
                return None

            root = TreeNode(pre_order[0])
            mid = in_order.index(root.val)
            root.left = build(pre_order[1:mid+1], in_order[:mid])
            root.right = build(pre_order[mid + 1:], in_order[mid + 1:])

            return root
        
        return build(preorder, inorder)
