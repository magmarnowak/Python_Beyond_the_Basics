class YourClass(object):
    classy = 'class value!'

dd = YourClass()

print dd.classy             # 'class value!''

dd.classy = 'inst value!'

print (dd.classy)           # 'inst value!'

del dd.classy               # 'inst value!'

print dd.classy             # 'class value!'

# When we look for an attribute, Python looks for it first in the instance,
# and then in the class. => THE ATTRIBUTE LOOK-UP ORDER
# Hence the deleted attribute is the instance one.
