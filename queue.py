"""
different kind of queue implementation

enqueue
dequeue
size
traverse

"""

class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            del self.queue[0]
        else:
            raise IndexError

    def is_empty(self):
        return 0 == len(self.queue)

    def size(self):
        return len(self.queue)

obj = Queue()

print obj.is_empty()
print obj.size()

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)

print obj.is_empty()
print obj.size()

obj.dequeue()
obj.dequeue()
obj.dequeue()

print obj.is_empty()
print obj.size()
