class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None

    def get(self, key):
        if key not in self.data:
            return -1
        else:
            node = self.data[key]
            self.remove(node)
            self.add(node)
            return node

    def put(self, key, value):
        if key not in self.data:
            node = Node(key, value)
            self.add(node)
            self.data[key] = node
        else:
            if len(self.data) <= self.capacity:
                node = self.data[key]
                self.remove(node)
                del self.data[key]
            else:
                node = Node(key, value)
                self.add(node)
                self.data[key] = node


