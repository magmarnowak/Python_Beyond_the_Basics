import random

class MyClass(object):
    def doThis(self):
        self.rand_val = random.randint(1,10)

myinst = MyClass()      # creates instance
myinst.doThis()         # calls method
print myinst.rand_val   # accesses the instance attribute

print ; print
