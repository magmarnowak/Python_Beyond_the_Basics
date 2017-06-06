#!/usr/bin/python

import pickle

class MyClass(object):

    def __init__(self, init_val):
        self.val = init_val

    def increment(self):
        self.val += 1

cc = MyClass(5)
cc.increment()
cc.increment()

with open('datafile.txt', 'w') as fh:
    pickle.dump(cc, fh)

with open('datafile.txt') as fh:
    unpickled_cc = pickle.load(fh)

print unpickled_cc
print unpickled_cc.val
