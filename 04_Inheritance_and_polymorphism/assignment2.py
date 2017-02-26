import abc
import datetime

class WriteFile(object):
    """Abstract class
    Contains common functionality for LogFile and DelimFile"""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def write(self):
        return


class LogFile(WriteFile):
    """Writes a log message to the file"""

    def __init__(self, filename):
        self.filename = filename

    def write(self, input):
        # needs to be improved, currently overrides logs, leaving only the latest one
        """Writes date, time and contents of a log message to a file.
        Date and time format: yyyy-mm-dd hh:mm
        input: str"""
        self.message = input
        # run strftime() on the current date-time returned by datetime.now()
        self.date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.log = self.date + " " + self.message + "\n"
        with open(self.filename, 'a') as self.file:
            self.file.write(self.log)

class DelimFile(WriteFile):
    """Writes a csv-like output"""

    def __init__(self, filename, delimiter):
        self.filename = filename
        self.delimiter = delimiter

    def write(self, input):
        """Writes a list of values separated by a delimiter to the file
        input: list
        output: str"""
        self.output = (self.delimiter + ' ').join(input)
        with open(self.filename, 'a') as self.file:
            self.file.write(self.output+'\n')
