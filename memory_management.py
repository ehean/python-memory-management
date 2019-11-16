import sys, gc
from pprint import pprint

print("Start: %s" % gc.get_count()[0])

def printRefCount(s):
    print("%s: %s" % (s, gc.get_count()[0])) #-478)

printRefCount("post printRefCount()")

class MyClass:
    printRefCount("post MyClass def (internal)")
    def __init__(self, object=None):
        printRefCount("post MyClass.__init__ def")
        self.next = object
        printRefCount("post MyClass.next def")

print("MyClass refcount: %s" % sys.getrefcount(MyClass))
for val in gc.get_referrers(MyClass):
    pprint(val)
    #pprint("MyClass referers: %s" % gc.get_referrers(MyClass))
printRefCount("post MyClass def")

# d -> c -> b (None)
def createObjects():

    printRefCount("top of createObjects()")
    a = MyClass()

    printRefCount("post a init")
    b = MyClass()

    printRefCount("post b init")
    c = MyClass(b)
    
    printRefCount("post c init")
    d = MyClass(c)

    printRefCount("post d init")
    return d

printRefCount("post createObjects() def")

r = createObjects()
printRefCount("post r init")
del r
printRefCount("post r delete")

