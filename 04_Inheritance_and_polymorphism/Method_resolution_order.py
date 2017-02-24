class A(object):

    def dothis(self):
        print "doing this in A"

class B(A):
    pass

class C(A):

    def dothis(self):
        print "doing this in C"

class D(B, C):
    pass

d_instance = D()
# check the class from which the method dothis will be inherited
d_instance.dothis()

# check the Method Resolution Order (mro):
print D.mro()
# mro is: D, B, C, A
# the first appearance of A (as a super class of B) is removed from the mro,
# as it is earlier in the look-up tree
