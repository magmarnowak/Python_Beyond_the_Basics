# Assignment 1

# Create a simple class, MaxSizeList, that acts a little bi like a list,
#with a pre-configured limit on its size.

class MaxSizeList(object):

    def __init__(self, maxLen):        # step 1
        self.maxLen = maxLen
        self.maxList = []

    def push(self, item):              # step 2 to be implemented
        if len(self.maxList) < self.maxLen:
            self.maxList.append(item)
        else:
            self.maxList.pop(0)
            self.maxList.append(item)

    def get_list(self):                # step 3 to be implemented
        return self.maxList

# test calling code below
a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print a.get_list()
print b.get_list()

# Step 1: initialise the instance with an empty aList and a max len of that list
# Step 2: If len(maxList) < maxLen get the argument of instance.push() and
#         append it to the list
#         Else: Pop the first element of that list and append the argument of
#         instance.push()
# Step 4: Return the list via a getter method
