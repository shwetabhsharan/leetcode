class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        popped = self.head
        popped.next = None
        next = self.head.next
        self.head = next
        return popped.value

    def peak(self):
        if self.head is not None:
            return self.head
        else:
            return None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count

    def traverse(self):
        current = self.head
        while current is not None:
            print current.value
            current = current.next

obj = Stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print obj.peak()
print obj.size()
print obj.pop()
print obj.traverse()