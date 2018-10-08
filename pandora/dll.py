"""
doubly linked list

add
traverse
size
delete
insert
get_previous
get_next
search

"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL(object):
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
        return cnt

    def add(self, value):
        node = Node(value)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def delete(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                curr.next = None
                curr.prev = None
                break
            else:
                curr = curr.next
        else:
            print "Element not found"

    def search(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                print "Found"
                break
            else:
                curr = curr.next
        else:
            print "Element not found"

    def get_previous(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr.prev
            else:
                curr = curr.next
        else:
            print "Index error"

    def get_next(self, value):
        curr = self.head
        while curr is not None:
            if curr.value == value:
                return curr.next
            else:
                curr = curr.next
        else:
            print "Index error"

obj = DLL()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
obj.traverse()
print "Size: ", obj.size()
obj.delete(3)
print"-"*10
obj.traverse()
obj.search(1)
obj.search(10)
print obj.get_previous(2).value
print obj.get_next(2).value