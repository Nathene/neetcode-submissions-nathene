# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            curr_end = None
            for _ in range(len(q)):
                curr_end = q.popleft()
                if curr_end.left:
                    q.append(curr_end.left)
                if curr_end.right:
                    q.append(curr_end.right)
            res.append(curr_end.val)
        
        return res