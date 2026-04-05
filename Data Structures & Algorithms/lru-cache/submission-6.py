class Node:
    def __init__(self, key: int, val: int, next: "Node" = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.val_to_node = {}
        self.dummy_tail = Node(-1, -1)
        self.dummy_head = Node(-1, -1, self.dummy_tail)
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.val_to_node:
            return -1
        node = self.val_to_node[key]
        val = node.val
        self.remove(key)
        self.insert(key, val)
        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.val_to_node:
            self.remove(key)
        elif self.size >= self.cap:
            self.remove(self.dummy_tail.prev.key)
        else:
            self.size += 1
        
        self.insert(key, value)

    def remove(self, key) -> None:
        if key not in self.val_to_node:
            return None
        node = self.val_to_node.pop(key)
        node.prev.next = node.next
        node.next.prev = node.prev
        node = None

    def insert(self, key: int, value: int) -> None:
        node = Node(key, value)
        self.val_to_node[key] = node
        
        tmp = self.dummy_head.next
        self.dummy_head.next = node
        node.prev = self.dummy_head
        node.next = tmp
        tmp.prev = node