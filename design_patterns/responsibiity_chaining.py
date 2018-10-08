"""
Chain of responsibility is a behavioral pattern that processes a request
through a series of processor objects. The request is sent from one
handler object to another handler object. All the handlers are part of
the chain.
"""

class Event(object):
    def __init__(self, name):
        self.name = name

class Handler(object):
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, event):
        handler = 'Handle ' + event