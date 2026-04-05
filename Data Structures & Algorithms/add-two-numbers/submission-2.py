# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = l1 if l1 else Node(0)
        l2 = l2 if l2 else Node(0)

        def dfs(node1: ListNode, node2: ListNode, carry: int) -> ListNode:
            if not node1 and not node2 and carry == 0:
                return None
            val_1 = node1.val if node1 else 0
            val_2 = node2.val if node2 else 0

            total = val_1 + val_2 + carry
            rem = total % 10
            carry = total // 10

            root = ListNode(rem)
            root.next = dfs(node1.next if node1 else None, node2.next if node2 else None, carry)

            return root
        return dfs(l1, l2, 0)

        
