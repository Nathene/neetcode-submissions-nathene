"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        new_head = Node(node.val)
        seen = {}
        seen[node.val] = new_head

        def dfs(old_node, new_node):
            if not old_node or not new_node:
                return

            for child in old_node.neighbors:
                if child.val not in seen:
                    new_child = Node(child.val)
                    new_node.neighbors.append(new_child)
                    seen[child.val] = new_child
                    dfs(child, new_child)
                else:
                    new_node.neighbors.append(seen[child.val])


        
        
        dfs(node, new_head)
        
        return new_head


