"""
LRU Cache

always maintain head and tail node as markers

"""

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

    def add(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def traverse(self):
        curr = self.head
        while curr is not None:
            print curr.key, curr.value
            curr = curr.next

    def get(self, key):
        if key not in self.data:
            return -1
        else:
            node = self.data[key]
            self.remove(node)
            self.add(node)
            return node

    def put(self, key, value):
        if key in self.data:
            node = self.data[key]
            self.remove(node)
            self.add(node)
            self.data[key].value = value
        else:
            if len(self.data) >= self.capacity:
                prev_node = self.tail.prev
                key = prev_node.key
                self.remove(prev_node)
                del self.data[key]

            node = Node(key, value)
            self.data[key] = node
            self.add(node)


cache = LRUCache(capacity=2)

cache.put('ham', 1)
cache.put('spam', 'eggs')

assert cache.get('spam') == 'eggs'
assert cache.get('ham') == 1

cache.put('baked beans', 'off')

assert cache.get('baked beans') == 'off'
assert cache.get('ham') == 1
assert cache.get('spam') is None