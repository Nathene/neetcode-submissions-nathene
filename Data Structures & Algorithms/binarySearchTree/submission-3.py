class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = Node(key, val)
        if not self.root:
            self.root = new_node
        
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1


    def getMin(self) -> int:
        curr = self._find_min(self.root)
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr =self.root
        while curr:
            if not curr.right:
                return curr.val
            curr = curr.right
        return -1

    def remove(self, key: int) -> None:
        self.root = self._remove_helper(self.root, key)
    
    def _remove_helper(self, curr, key) -> Node:
        if curr is None:
            return None
        
        if key > curr.key:
            curr.right = self._remove_helper(curr.right, key)
        elif key < curr.key:
            curr.left = self._remove_helper(curr.left, key)
        else:
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left
            else:
                min_node = self._find_min(curr.right)
                curr.key = min_node.key
                curr.val = min_node.val
                curr.right = self._remove_helper(curr.right, min_node.key)
        
        return curr
    def _find_min(self, node):
        while node and node.left:
            node = node.left
        return node if node else None

    def getInorderKeys(self) -> List[int]:
        def _generate(node):
            if not node:
                return
            yield from _generate(node.left)
            yield node.key
            yield from _generate(node.right)
        
        return list(_generate(self.root)) if self.root else []

