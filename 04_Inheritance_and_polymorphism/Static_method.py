class InstanceCounter(object):
    count = 0                   # class attrubute = data shared among instances

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count +=1 # access class attribute and increment it

    @ staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)
d = InstanceCounter('hello')

print a.val
print b.val
print c.val
print d.val
