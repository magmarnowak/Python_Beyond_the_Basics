import abc
import datetime

class WriteFile(object):
    """Abstract class
    Contains common functionality for LogFile and DelimFile"""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        with open(self.filename, 'a') as self.file:
            self.file.write(text + '\n')

class LogFile(WriteFile):
    """Writes a log message to the file"""

    def write(self, input):
        """Writes date, time and contents of a log message to a file.
        Date and time format: yyyy-mm-dd hh:mm
        input: str"""
        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.log = self.date + " " + input
        self.write_line(self.log)

class DelimFile(WriteFile):
    """Writes a csv-like output"""

    def __init__(self, filename, delimiter):
        super(DelimFile, self).__init__(filename)
        self.delimiter = delimiter

    def write(self, input):
        """Writes a list of values separated by a delimiter to the file
        input: list
        output: str"""
        self.output = ''
        for x in input:
            # put values that include a comma into double-quotes:
            if ',' in x:
                self.output += '\"'+x+'\"' + self.delimiter + ' '
            else:
                self.output +=  x + self.delimiter + ' '
        self.output = self.output[:-2]
        self.write_line(self.output)
