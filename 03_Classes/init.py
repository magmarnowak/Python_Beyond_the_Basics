class MyNum(object):
    def __init__(self):
        print "calling __init__"
        self.val = 0
    def increment(self):
        self.val += 1

dd = MyNum()        # init is executed automatically when an instance is created
dd.increment()
dd.increment()
print dd.val        # accessing the instance attribute

print
