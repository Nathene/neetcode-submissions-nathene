"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy_head = Node(-1)
        copy_head = dummy_head
        curr = head


        node_random_map = { None: None }
        while curr:
            new_node = Node(curr.val)
            node_random_map[curr] = new_node
            copy_head.next = new_node
            copy_head = copy_head.next
            curr = curr.next
        
        curr = head
        copy_head = dummy_head.next
        while curr:
            random_node = curr.random
            if random_node:
                copy_head.random = node_random_map[random_node]
            curr = curr.next
            copy_head = copy_head.next
        
        return dummy_head.next


       
        