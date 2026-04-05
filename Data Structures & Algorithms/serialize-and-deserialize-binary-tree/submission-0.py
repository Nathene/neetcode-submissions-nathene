class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#,"
        return f"{root.val},{self.serialize(root.left)}{self.serialize(root.right)}"
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        self.index = 0
        
        def dfs():
            if nodes[self.index] == "#":
                self.index += 1
                return None
            
            root = TreeNode(int(nodes[self.index]))
            self.index += 1
            root.left = dfs()
            root.right = dfs()
            return root
            
        return dfs()