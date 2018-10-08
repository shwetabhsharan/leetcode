"""
singly linked list - operations

add
traverse
insert
delete
size

"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def traverse(self):
        curr = self.head
        while curr is not None:
            print curr.value
            curr = curr.next

    def size(self):
        curr = self.head
        size = 0
        while curr is not None:
            size = size + 1
            curr = curr.next
        return size

    def delete(self, value):
        curr = self.head
        prev = None
        while curr is not None:
            if curr.value == value:
                next_node = curr.next
                prev.next = next_node
                curr.next = None
                break
            else:
                prev = curr
                curr = curr.next
        else:
            print "Element not found"

    def insert(self, value, pos):
        if pos > self.size() - 1:
            raise IndexError
        else:
            curr = self.head
            cnt = 0
            while curr is not None:
                if cnt == pos:
                    node = Node(value)
                    next_node = curr.next
                    curr.next = node
                    node.next = next_node
                    break
                else:
                    cnt = cnt + 1
                    curr = curr.next

obj = SLL()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
obj.traverse()
print "Total Size:", obj.size()
obj.delete(4)
obj.traverse()
obj.insert(10, 10)
obj.insert(6, 0)
obj.traverse()