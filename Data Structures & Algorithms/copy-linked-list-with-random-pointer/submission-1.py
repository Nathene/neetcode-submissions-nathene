class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # we can use a pattern called 'interleaving'
        # which means instead of storing the nodes in a map, we can 
        # append the new copied node, directly next to the original. 
        # This way, we can return the new copied list which lives quite closely to the original

        curr = head
        while curr:
            new_node = Node(curr.val)
            tmp = curr.next
            curr.next = new_node
            new_node.next = tmp
            curr = tmp
        
        # Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Separate the lists
        dummy = Node(-1)
        copy_curr = dummy
        curr = head
        while curr:
            copy_curr.next = curr.next
            curr.next = curr.next.next
            
            curr = curr.next
            copy_curr = copy_curr.next
        
        return dummy.next