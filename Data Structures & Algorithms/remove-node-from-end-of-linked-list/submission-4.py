# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head

        depth = 0
        first = head
        while first:
            depth += 1
            first = first.next
        
        needed_node = depth - n
        depth = 0
    
        second = dummy_head
        while second:
            if depth == needed_node:
                second.next = second.next.next
                break
            depth += 1
            second = second.next
        
        return dummy_head.next
                

