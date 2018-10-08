"""
LRU Cache implementation in Python
Cache replacement policy

Access Sequence
A B C D E D F

{1: A}
{1: A, 2: B}
{1: A, 2: B, 3: C}
{1: A, 2: B, 3: C, 4: D}

Now cache is full so adding E will remove A: 1 as it is least recently used

{2: B, 3: C, 4: D, 5: E}

Now D is being added which is already present so we refresh cache

{2: B, 3: C, 6: D, 5: E}

get(key) -1 in case of no value
put(key, value)

https://www.youtube.com/watch?v=R0GTqg3pJKg&frags=pl%2Cwn

"""

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dict:
            n = self.dict[key]
            self._remove(n)
            self._add(n)
            return n.value
        return -1

    def put(self, key, value):
        if key in self.dict:
            self._remove(self.dict[key])
        n = Node(key, value)
        self._add(n)
        self.dict[key] = n
        if len(self.dict) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dict[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

cache = LRUCache(capacity=2)

cache.put('ham', 1)
cache.put('spam', 'eggs')

assert cache.get('spam') == 'eggs'
assert cache.get('ham') == 1

cache.put('baked beans', 'off')

assert cache.get('baked beans') == 'off'
assert cache.get('ham') == 1
assert cache.get('spam') is None