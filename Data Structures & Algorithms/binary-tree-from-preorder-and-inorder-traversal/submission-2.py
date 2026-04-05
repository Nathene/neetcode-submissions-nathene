# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(in_order, pre_order) -> TreeNode:
            if not pre_order or not in_order:
                return None

            root = TreeNode(pre_order[0])
            mid = in_order.index(root.val)
            root.left = build(in_order[:mid], pre_order[1:mid+1])
            root.right = build(in_order[mid + 1:], pre_order[mid + 1:])

            return root
        
        return build(inorder, preorder)
