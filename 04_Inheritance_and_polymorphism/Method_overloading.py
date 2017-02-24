import abc

class GetSetParent(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):

    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)

    def showdoc(self):
        print 'GetSetInt object (%r) only accepts integer values' % (id(self))

class GetSetList(GetSetParent):
    def __init__(self, value =0):
        self.vallist = [value]

    def get_val(self):
        """Returns the last set value"""
        return self.vallist[-1]

    def get_vals(self):
        """Returns a list of all the values set"""
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print "GetSetList object, len %d, stores history of values set" % len(self.vallist)

# test run code for GetSetInt
x = GetSetInt(5)
y = GetSetInt('yum')
print x.get_val() # 0, inherited from GetSetParent
x.set_val(3)
y.set_val(7)
print x.get_val() # 3
print y.get_val() # 7
y.set_val('yum')
print y.get_val() # 0, set by set_val in GetSetInt
x.showdoc()
y.showdoc()
# test run code for GetSetList
gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)
print gsl.get_val()
print gsl.get_vals()
gsl.showdoc()
