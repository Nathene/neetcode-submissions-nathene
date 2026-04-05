class Node:
    def __init__(self, val: int, next=None):
        self.next = next
        self.val = val


class MyHashSet:

    def __init__(self):
        self.cap = 1000
        self.my_set = [None] * self.cap 

    def add(self, key: int) -> None:
        if self.contains(key): return
        if not self.my_set[key%self.cap]:
            self.my_set[key%self.cap] = Node(key)
        else:
            head = self.my_set[key%self.cap]
            while head.next:
                head = head.next
            head.next = Node(key)

    def remove(self, key: int) -> None:
        if not self.contains(key): return

        head = self.my_set[key%self.cap]
        if head.val == key:
            self.my_set[key%self.cap] = head.next
            return
        while head.next and head.next.val != key:
            head = head.next
        head.next = head.next.next



    def contains(self, key: int) -> bool:
        if self.my_set[key%self.cap] == None:
            return False
        head = self.my_set[key%self.cap]
        while head:
            if head.val == key:
                return True
            head = head.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)