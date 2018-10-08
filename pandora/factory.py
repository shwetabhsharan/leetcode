class Star(object):
    def __init__(self):
        print "*"

class Percent(object):
    def __init__(self):
        print "%"

class Hash(object):
    def __init__(self):
        print "#"

def caller(name):
    globals()[name]()

caller("Star")
caller("Percent")
caller("Hash")