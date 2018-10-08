"""
Linkedlist implementation in Python, following operations are implemented
1. Add - 
2. Searching - 
3. Remove - 
4. Append - 
5. Index
6. Insert
7. Size - 
8. Traverse - 
9. Find the middle node value
"""

class Node(object):
    """
    New node structure
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    """
    Linked List class
    """
    def __init__(self):
        """
        always maintain the head node to indicate the entry point
        """
        self.head = None

    def add(self, item):
        """
        create new node
        make new node as head node
        assign new node's next as head (head pointing to current)
        """
        node = Node(item)
        node.next = self.head
        self.head = node

    def traverse(self):
        """
        check if current is null, if not, print value and traverse
        """
        current = self.head
        while current is not None:
            print current.value
            current = current.next

    def search(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                print "Found"
                break
            else:
                current = current.next
        else:
            print "Not Found"

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.next
        print count

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.value == item:
                previous.next = current.next
                current.next = None
                break
            else:
                previous = current
                current = current.next
        else:
            print "Item not present"

    def insert(self, item, index):
        pass

obj = LinkedList()
obj.add(1)
obj.add(2)
obj.add(3)
obj.add(4)
obj.add(5)
obj.add(6)
obj.add(7)
obj.add(8)
obj.add(9)
obj.traverse()
obj.search(2)
obj.size()
obj.remove(5)
obj.traverse()