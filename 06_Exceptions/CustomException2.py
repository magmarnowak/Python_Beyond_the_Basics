class MyError(Exception):
    def __init__(self, *args):
        print("calling init")
        if args:
            self.message =args[0]
        else:
            self.message = None

    def __str__(self):
        print("calling str")
        if self.message:
            return "here's a MyError exception with message:   {0}".format(self.message)
        else:
            return"here's a MyError exception!"

# raise MyError

raise MyError('Houston, we have a problem')
