class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def find_smallest_child(node: TreeNode) -> TreeNode:
            if not node:
                return None
            
            if not node.left:
                return node

            if node.left:
                return find_smallest_child(node.left)
            

        def find_and_delete(node: TreeNode) -> Optional[TreeNode]:
            if not node:
                return None
            
            if node.val == key:
                # found our node to delete
                if not node.right:
                    return node.left
                # otherwise 
                if not node.left:
                    return node.right
                
                smallest = find_smallest_child(node.right)
                node.val = smallest.val
                node.right = delete_min(node.right)
                return node
            
            if node.val > key:
                node.left = find_and_delete(node.left)
            else:
                node.right = find_and_delete(node.right)
            
            return node

        def delete_min(node: TreeNode) -> Optional[TreeNode]:
            if not node.left:
                return node.right
            node.left = delete_min(node.left)
            return node
        
        return find_and_delete(root)