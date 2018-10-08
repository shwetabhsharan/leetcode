"""
enqueue
dequeue
size
traverse

Queue Implementation using SLL

"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue(object):
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head = node

    def dequeue(self):
        cnt = 0
        curr = self.head
        prev = None
        while curr is not None:
            cnt = cnt + 1
            if cnt == self.size():
                prev.next = None
                curr.value = None
            else:
                prev = curr
                curr = curr.next

    def traverse(self):
        curr = self.head
        while curr is not None:
            print curr.value
            curr = curr.next

    def size(self):
        cnt = 0
        curr = self.head
        while curr is not None:
            cnt = cnt + 1
            curr = curr.next
        return cnt

obj = Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)

obj.traverse()
obj.dequeue()
obj.traverse()