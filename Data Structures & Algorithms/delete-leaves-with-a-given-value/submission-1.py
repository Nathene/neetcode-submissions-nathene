# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        # 1. no left child <-- 
        # 2. no right child <-- 
        # 3. both children 
        # 4. no children <--

        def delete_node(node: TreeNode) -> TreeNode:
            if not node:
                return None
            

            node.left = delete_node(node.left)
            node.right = delete_node(node.right)
            if not node.left and not node.right and node.val == target:
                return None
            
            return node
            
        
        return delete_node(root)
                
                

