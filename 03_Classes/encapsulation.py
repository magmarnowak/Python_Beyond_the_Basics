class MyClass(object):
    def set_val(self, val):
        self.value = val # set_val takes the argument val and sets it as an
        # attribute in the instance under the name value
        #set_val is a SETTER method - it sets a value in the instance
    def get_val(self):
        return self.value
        #get_val is a GETTER method
