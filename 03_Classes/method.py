class Joe(object):
    def callMe(self):
         print "calling callMe method with instance"
         print self

thisJoe = Joe()     # creates an instance
print thisJoe       # <__main__.Joe object at 0x0275F4D0>
thisJoe.callMe()    # 'calling callMe method with instance',
                    # <__main__.Joe object at 0x0275F4D0>
print; print
