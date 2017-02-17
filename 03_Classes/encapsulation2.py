class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val =val
    def get_val(self):
        return self.val

    def increment_val(self):
        self.val += 1

i = MyInteger()
i.set_val(9)
print i.get_val()
i.set_val('hi')         #this value is not set as it is caught as a Value Error
print i.get_val()       #this is still 9 since "hi" was caught as an Error
print i.increment_val()
i.val = 'hi' #this sets the value of the attribute directly, w/out calling
#the setter method. Hence, it is not caught as an error and can impair the
#integrity of the instance's data

print i.increment_val() #now this will cause an error because val is not of type
# int
