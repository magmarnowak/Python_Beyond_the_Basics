class Date(object):
    def get_date(self):
        return '2014-10-13'

class Time(Date):
    def get_time(self):
        return '08:13:07'

dt = Date()
print dt.get_date()

tm = Time()
print tm.get_time()
print tm.get_date()
