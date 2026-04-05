class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.size = 0
    
    def hash_function(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        head = self.buckets[index]
        if not head:
            self.buckets[index] = Node(key, value)
        else:
            while head.next:
                if head.key == key:
                    head.val = value
                    return
                head = head.next
            if head.key == key:
                head.val = value
                return
            head.next = Node(key, value)
        self.size += 1
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        head = self.buckets[index]
        while head:
            if head.key == key:
                return head.val
            head = head.next

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        head = self.buckets[index]
        prev = None

        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.buckets[index] = head.next
                self.size -= 1
                return True
            prev, head = head, head.next

        return False

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_buckets = [None] * self.capacity
        for node in self.buckets:
            while node:
                index = node.key % self.capacity
                if new_buckets[index] is None:
                    new_buckets[index] = node
                else:
                    head = new_buckets[index]
                    node.next = head
                    new_buckets[index] = node
                node = node.next
        self.buckets = new_buckets
            
     
