class YourClass(object):
    classy = 10             # variable set in the class

    def set_val(self):
        self.insty = 100    # attribute set in the instance

dd = YourClass()

dd.set_val()
print dd.classy # the instance has access both to the variable set in the class
print dd.insty  # and the attribute set in the instance
print
