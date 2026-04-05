class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.dummy_head = Node(-1)
        self.dummy_tail = Node(-1)

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.curr_cap = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
             
        tmp = self.dummy_tail.prev 
        new_node = Node(value)
        self.dummy_tail.prev = new_node
        new_node.next = self.dummy_tail
        new_node.prev = tmp
        tmp.next = new_node
        self.curr_cap += 1

        return True

    def deQueue(self) -> bool:
        
        if not self.isEmpty():
            self.dummy_head.next = self.dummy_head.next.next
            self.curr_cap -= 1
            return True
        
        return False
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.dummy_head.next.val
        
        return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.dummy_tail.prev.val
        
        return -1


    def isEmpty(self) -> bool:
        return self.curr_cap == 0

    def isFull(self) -> bool:
        return self.curr_cap == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()