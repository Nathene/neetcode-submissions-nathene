# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # step 1: find where we want to insert into the tree

        new_node = TreeNode(val)

        if not root:
            return new_node

        def find(node: TreeNode) -> None:
            if not node:
                return
            
            if node.val > val:
                if node.left:
                    find(node.left)
                else:
                    node.left = new_node
                    return
            else:
                if node.right:
                    find(node.right)
                else:
                    node.right = new_node
                    return


        find(root)

        return root            
        # step 2: if there is children, will have to deal with that eventually

