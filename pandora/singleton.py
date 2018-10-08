class Singleton(object):
    instance = None
    def __init__(self):
        if Singleton.instance is not None:
            raise Exception("object already exists")
        else:
            Singleton.instance = True

obj1 = Singleton()
obj2 = Singleton()