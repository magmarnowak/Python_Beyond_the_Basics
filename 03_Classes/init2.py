class MyNum(object):
    def __init__(self, value):
        try:                   # the try-except serves as an integrity gate
            value = int(value) # ensuring the instance is initialised on an int
        except ValueError:     # otherwise it raises an exception
            value = 0          # and sets the value of an instance to 0
        self.val = value
    def increment(self):
        self.val += 1

aa = MyNum('hello')         # creating an instance and calling __init__
bb = MyNum(100)             # creating an instance and calling __init__
aa.increment()
aa.increment()
bb.increment()
print aa.val                # 2
print bb.val                # 101

print
