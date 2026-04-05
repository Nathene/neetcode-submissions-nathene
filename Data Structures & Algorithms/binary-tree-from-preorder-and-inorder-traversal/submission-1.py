# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. THE HASH MAP: 
        # Instead of searching the inorder list for the root index (O(N)), 
        # we do a one-time pass to store indices for O(1) lookup.
        in_map = {val: i for i, val in enumerate(inorder)}
        
        # 2. THE GLOBAL POINTER:
        # Instead of slicing the preorder list, we just keep track of 
        # which element we are currently looking at.
        self.pre_idx = 0

        def helper(left, right):
            # BASE CASE:
            # If the boundaries cross, there are no nodes in this subtree.
            if left > right:
                return None

            # PICK THE ROOT:
            # The current element in preorder is always the root of the 
            # current subtree we are building.
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            # Move the global pointer to the next root for the next call.
            self.pre_idx += 1

            # FIND THE SPLIT:
            # Everything to the left of 'mid' in the inorder array belongs 
            # to the left subtree. Everything to the right belongs to the right.
            mid = in_map[root_val]

            # RECURSE:
            # Crucial: We must build the LEFT subtree first because the 
            # next element in the preorder list is the root of the left subtree.
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root

        # Start the recursion with the full range of the inorder list.
        return helper(0, len(inorder) - 1)