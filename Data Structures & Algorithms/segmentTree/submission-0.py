class Node:
    def __init__(self, total: int, left: int, right: int):
        self.sum = total
        self.left = left
        self.right = right
        self.left_child = None
        self.right_child = None


class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums: list[int], left: int, right: int) -> Node:
        if left == right:
            return Node(nums[left], left, right)

        root = Node(0, left, right)

        mid = (left + right) // 2 
        
        root.left_child = self.build(nums, left, mid)
        root.right_child = self.build(nums, mid+1, right)

        root.sum = root.left_child.sum + root.right_child.sum

        return root
    
    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root: Node, index: int, val: int) -> None:
        if root.left == root.right:
            root.sum = val
            return 

        mid = (root.left + root.right) // 2

        if index > mid:
            self.update_helper(root.right_child, index, val)
        else:
            self.update_helper(root.left_child, index, val)
        
        root.sum = root.left_child.sum + root.right_child.sum
    
    def query(self, left: int, right: int) -> int:
        return self.query_helper(self.root, left, right)
    
    def query_helper(self, root: Node, left: int, right: int) -> int:
        if root.left > right or left > root.right:
            return 0
        
        if left <= root.left and right >= root.right:
            return root.sum
        
        return self.query_helper(root.left_child, left, right) + self.query_helper(root.right_child, left, right)