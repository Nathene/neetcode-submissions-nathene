class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.arr = [None] * 10007
        self.cap = len(self.arr)

    def put(self, key: int, value: int) -> None:
        index = key % self.cap

        new_node = Node(key, value)
        curr = self.arr[index]
        if not curr:
            self.arr[index] = new_node
            return
        
        while curr:
            if key == curr.key:
                curr.val = value
                return
            
            if curr.next == None:
                curr.next = new_node
                return
    

    def get(self, key: int) -> int:
        if not self.contains(key): return -1
        index = key % self.cap
        curr = self.arr[index]

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> None:
        if not self.contains(key): return

        index = key % self.cap
        curr = self.arr[index]
        if curr.key == key:
            self.arr[index] = curr.next
        else:
            while curr and curr.next:
                if curr.next.key == key:
                    curr.next = curr.next.next
                curr = curr.next
        
    def contains(self, key: int) -> bool:
        index = key % self.cap
        if self.arr[index] == None:
            return False
        
        curr = self.arr[index]

        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)