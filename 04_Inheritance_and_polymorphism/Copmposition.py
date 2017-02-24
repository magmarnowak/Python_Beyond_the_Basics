import random
import StringIO

class WriteMyStuff(object):

    def __init__(self, writer):
        self.writer = writer

    def write(self):
        write_text = "this is a silly message"
        self.writer.write(write_text)

# create a file object
fh = open('test.txt', 'w')
# pass the file object to WriteMyStuff
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

# create a StringIO
sioh = StringIO.StringIO()
# pass it to WriteMyStuff
w2 = WriteMyStuff(sioh)
# call write() on StringIO
w2.write()

print 'file object: ', open('test.txt', 'r').read()
print 'StringIO object: ', sioh.getvalue()
