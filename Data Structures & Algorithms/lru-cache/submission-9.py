class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head: Node = Node(-1, -1)
        self.tail: Node = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.lookup: dict[int, Node] = defaultdict(Node)    

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        node = self.lookup[key]
        self._remove(key)
        self._insert(node.key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        self._remove(key)
        self._insert(key, value)

        if len(self.lookup) > self.capacity:
            self._remove_last()
    
    def _remove(self, key: int) -> None:
        if key not in self.lookup: return

        node = self.lookup[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        del self.lookup[key]
    
    def _remove_last(self) -> None:
        node = self.head.next
        del self.lookup[node.key]
        self.head.next = self.head.next.next
        node.next.prev = self.head

    
    def _insert(self, key: int, val: int) -> None:
        new_node: Node = Node(key, val)
        self.lookup[key] = new_node

        old_tail = self.tail.prev
        old_tail.next = new_node
        new_node.prev = old_tail
        new_node.next = self.tail
        self.tail.prev = new_node


        

