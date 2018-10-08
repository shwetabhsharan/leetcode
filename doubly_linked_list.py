"""
Implementation do doubly linked list using Node concept
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def traverse(self):
        curr = self.head
        while curr is not None:
            print curr.data
            curr = curr.next

    def add(self, data):
        node = Node(data) # create new node
        node.next = self.head # assign new node next to head
        if self.head is not None:
            self.head.prev = node # assign head previous to node
        self.head = node # move head to current

    def size(self):
        count = 0
        curr = self.head
        while curr is not None:
            count = count + 1
            curr = curr.next
        return count

    def search(self, data):
        curr = self.head
        while curr is not None:
            if curr.data == data:
                print 'Found', curr.data
                break
            else:
                curr = curr.next
        else:
            print 'Not found'

    def insert(self, item, index):
        count = 0
        curr = self.head
        while curr is not None:
            if count == index:
                node = Node(item) # new node creation
                curr.next.prev = node
                node.next = curr.next
                node.prev = curr # node previous is curr
                curr.next = node
                break
            else:
                curr = curr.next
                count = count+1
        else:
            print 'index out of range'

    def delete(self, item):
        curr = self.head
        while curr is not None:
            if curr.data == item:
                prev = curr.prev
                prev.next = curr.next
                next = curr.next
                if next is not None:
                    next.prev = prev
                break
            else:
                curr = curr.next
        else:
            print "item not present in the list"

obj = DoublyLinkedList()
obj.add(0)
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
obj.traverse()
print "Size:", obj.size()
obj.search(41)
obj.insert(10, 4)
obj.traverse()
obj.delete(1)
obj.traverse()