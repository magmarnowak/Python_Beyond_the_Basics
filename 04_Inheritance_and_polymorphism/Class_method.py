# compare the code with data.py from Class chapter
class InstanceCounter(object):
    count = 0                   # class attrubute = data shared among instances

    def __init__(self, val):
        self.val = val
        InstanceCounter.count +=1 # access class attribute and increment it

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val
    @classmethod # decorator
    def get_count(cls):
        return cls.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)
d = InstanceCounter(29)

for obj in (a, b, c, d):
    print "val of obj: %s" % (obj.get_val())
    print "count: %s" % (obj.count)
