class Node:
    def __init__(self, val: int, key: int, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next   
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.cap = capacity
        self.curr = 0

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        node = self.mp[key]
        res = node.val
        self._remove(key)
        self._add_to_end(node)

        return res



    def put(self, key: int, value: int) -> None:
        
        if key in self.mp:
            self._remove(key)
        else:
            self.curr += 1

        node = Node(value, key)
        self._add_to_end(node)
        
        if self.curr > self.cap:
            evict_key = self.head.next.key
            self._remove(evict_key)
            self.curr -= 1
    
    def _remove(self, key: int):
        node = self.mp.pop(key)
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_end(self, node: Node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.mp[node.key] = node

        