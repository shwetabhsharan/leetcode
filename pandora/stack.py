"""
Stack implementation
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None

    def traverse(self):
        curr = self.head
        while curr is not None:
            print curr.value
            curr = curr.next

    def size(self):
        curr = self.head
        cnt = 0
        while curr is not None:
            cnt = cnt + 1
            curr = curr.next

    def peak(self):
        if self.head is not None:
            return self.head.value
        else:
            return -1

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head:
            node = self.head
            self.head = node.next
            node.next = None
            return node.value
        else:
            return -1

obj = Stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.traverse()
print "-"*10
obj.pop()
print "-"*10
obj.traverse()