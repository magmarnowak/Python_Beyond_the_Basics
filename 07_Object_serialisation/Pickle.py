#!/usr/bin/python

import pickle

# store object to a file

mylist = ['a', 'b', 'c', 'd']

with open("datafile.txt", "w") as fh:
    pickle.dump(mylist, fh)

with open("datafile.txt") as fh:
    unpickledlist = pickle.load(fh)

print unpickledlist

# store object to a str

x = pickle.dumps(['a', 'b', 'c', 'd', 1, 2.3])
var = pickle.loads(x)
print var
