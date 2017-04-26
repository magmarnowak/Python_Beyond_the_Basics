class MyClass(object):

    def __enter__(self):
        print("we have entered 'with'")
        return self

    def __exit__(self, type, value, traceback):
        print('we are leaving "with"')

    def sayhi(self):
        print("hi, instance %s" %(id(self)))

with MyClass() as cc:
    cc.sayhi()

print("after the 'with' block")
