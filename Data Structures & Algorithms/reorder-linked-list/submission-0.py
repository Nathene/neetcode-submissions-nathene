# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        if not head:
            return None

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None
        while second_half:
            stack.append(second_half)
            second_half = second_half.next
            

        
        # while the len(stack) >= stack_len // 2
        # tmp = head.next
        # head.next = stack.pop()
        # head.next.next = tmp
        # head = tmp
        curr = head
        while stack:
            tmp = curr.next
            curr.next = stack.pop()
            curr.next.next = tmp
            curr = tmp
        
        
    