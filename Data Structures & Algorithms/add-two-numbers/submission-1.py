class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def solve(node1, node2, opt=0):
            if not node1 and not node2 and opt != 0:
                return ListNode(opt)
            if not node1 and not node2:
                return None
            if not node1:
                sum_nodes = node2.val + opt
                new_node = ListNode(sum_nodes % 10)
                new_node.next = solve(None, node2.next, opt=sum_nodes // 10)
                return new_node
            if not node2:
                sum_nodes = node1.val + opt
                new_node = ListNode(sum_nodes % 10)
                new_node.next = solve(node1.next, None, opt=sum_nodes // 10)
                return new_node
            
            sum_nodes = node1.val + node2.val + opt
            new_node = ListNode(sum_nodes)
            if sum_nodes < 10:
                new_node.next = solve(node1.next, node2.next)
            else:
                rem = sum_nodes % 10
                val = sum_nodes // 10
                new_node.val = rem
                new_node.next = solve(node1.next, node2.next, opt=val)
            
            return new_node
        
        dummy = ListNode(-1)
        dummy.next = solve(l1, l2)
        return dummy.next