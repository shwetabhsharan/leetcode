"""
Implement string compression
aabbcddeeef
a2b2c1d2e3f1
"""

def string_compression(data):
    """
        
    """
    l2 = []
    l1 = [i for i in data]
    for i in l1:
        count = l1.count(i)
        if i not in l2:
            l2.append(i)
            l2.append(str(count))
    print "".join(l2)

string_compression("aabbcddeeef")