# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)

        curr = dummy_head
        for _ in range(left - 1):
            curr = curr.next
        
        before_rev = curr
        curr = curr.next
        
        prev = None
        sub_tail = curr
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        before_rev.next = prev
        sub_tail.next = curr
        
        return dummy_head.next