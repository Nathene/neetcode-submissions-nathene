class Node:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.arr = [None] * 10007
        self.cap = len(self.arr)

    def add(self, key: int) -> None:
        if self.contains(key): return 

        index = key % self.cap
        if self.arr[index] is None:
            self.arr[index] = Node(key)
            return
        
        curr = self.arr[index]
        while curr and curr.next:
            curr = curr.next
        
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return

        index = key % self.cap
        curr = self.arr[index]
        if curr.key == key:
            self.arr[index] = curr.next
        else:
            while curr and curr.next:
                if curr.next.key == key:
                    curr.next = curr.next.next                
        

    def contains(self, key: int) -> bool:
        index = key % self.cap
        if self.arr[index] is None:
            return False
        
        curr = self.arr[index]
        while curr:
            if curr.key == key:
                return True
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)