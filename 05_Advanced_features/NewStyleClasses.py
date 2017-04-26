# old style class
class OldClass():
    pass

# new style class
class NewClass(object):
    pass

oc = OldClass()

nc = NewClass()

print(type(oc))
print(type(nc))

print(oc.__class__) 
