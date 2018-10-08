"""
factory design pattern: factory design pattern is creational pattern
which does not exposes the logic implemented behind when creating the object.
"""

class Star(object):
    def __init__(self):
        print "*"

class Percent(object):
    def __init__(self):
        print "%"

class Hash(object):
    def __init__(self):
        print "#"

class Handler(object):
    def __init__(self, pattern):
        globals()[pattern]()

obj = Handler("Star")
obj = Handler("Percent")
obj = Handler("Hash")