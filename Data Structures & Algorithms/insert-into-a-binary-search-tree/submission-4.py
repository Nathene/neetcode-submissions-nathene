# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # step 1: find where we want to insert into the tree
        def find(node: TreeNode) -> None:
            if not node:
                return TreeNode(val)
            
            if node.val > val:
                node.left = find(node.left)
            else:
                node.right = find(node.right)
            
            return node

        return find(root)
        # step 2: if there is children, will have to deal with that eventually

