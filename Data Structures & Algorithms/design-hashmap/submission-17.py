class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.capacity = 10007
        self.my_array = [None] * self.capacity 

    def put(self, key: int, value: int) -> None:
        if not self.my_array[key%self.capacity]:
            self.my_array[key%self.capacity] = Node(key, value)
            return
        head = self.my_array[key%self.capacity]
        while head:
            if head.key == key:
                head.val = value
                return
            if not head.next:
                head.next = Node(key, value)
                return
            head = head.next


    def get(self, key: int) -> int:
        head = self.my_array[key%self.capacity]
        if not head:
            return -1
        while head:
            if head.key == key:
                return head.val
            head = head.next
        # return -1

    def remove(self, key: int) -> None:
        if self.get(key) == -1:
            return
        head = self.my_array[key%self.capacity]
        if head.key == key:
            self.my_array[key%self.capacity] = head.next
            return
        while head.next:
            if head.next.key == key:
                head.next = head.next.next
                return
            head = head.next
        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)