# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()

        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            q.append(root.val)
            dfs(root.right)

        dfs(root)

        while k > 1:
            _ = q.popleft()
            k -= 1
        
        return q.popleft()