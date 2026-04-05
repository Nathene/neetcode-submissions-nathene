class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        
        n = len(stack)
        counter = 0
        curr = head
        while counter < (n // 2):
            tmp = curr.next
            node_from_end = stack.pop()
            node_from_end.next = tmp
            curr.next = node_from_end
            curr = tmp
            counter += 1
        
        curr.next = None