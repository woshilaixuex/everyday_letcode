class LinkListNode:
    def __init__(self,key=-1,value=-1):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
# O(n) get   
class LRUCache0:
    def __init__(self, capacity: int):
        self.data = {}
        self.capacity = capacity
        self.head = LinkListNode()
        self.tail = LinkListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.data.keys():
            return -1
        node = self.head
        while(node.next):
            if node.key == key:
                break
            node = node.next
        # 取出node
        node.prev.next = node.next
        node.next.prev = node.prev
        # 重置node前后节点
        node.next = self.head.next
        node.prev = self.head
        # 重置node前后节点的后前
        node.prev.next = node
        node.next.prev = node
        return self.data[key]
    def put(self, key: int, value: int) -> None:
        if key not in self.data.keys():
            node = LinkListNode(key)
            node.prev = self.head
            node.next = self.head.next
            node.prev.next = node
            node.next.prev = node
            self.data[key] = value
        else:
            self.get(key)
            self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.pop(self.tail.prev.key)
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
# O(1)
class LRUCache:
    def __init__(self, capacity: int):
        self.data = {}
        self.capacity = capacity
        self.head = LinkListNode()
        self.tail = LinkListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def getNode(self, key: int) -> LinkListNode:
        if key not in self.data.keys():
            return None
        node = self.data[key]
        # 取出node
        node.prev.next = node.next
        node.next.prev = node.prev
        # 重置node前后节点
        node.next = self.head.next
        node.prev = self.head
        # 重置node前后节点的后前
        node.prev.next = node
        node.next.prev = node
        return self.data[key]
    def get(self, key: int) -> int:
        node = self.getNode(key)
        return node.value if node is not None else -1
    def put(self, key: int, value: int) -> None:
        if key not in self.data.keys():
            node = LinkListNode(key,value)
            node.prev = self.head
            node.next = self.head.next
            node.prev.next = node
            node.next.prev = node
            self.data[key] = node
        else:
            node = self.getNode(key)
            node.value = value
            self.data[key] = node
        if len(self.data) > self.capacity:
            self.data.pop(self.tail.prev.key)
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail         
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    cache.get(2)
    cache.put(3,3)
    cache.get(2)
    cache.put(4,4)
    cache.get(1)
    cache.get(3)
    cache.get(4)