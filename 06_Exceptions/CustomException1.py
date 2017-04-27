import re

def process_date(this_date=input('Please enter date:\n>>> ')):
    """(str)->str
    Given a date as a str validates if it's been entered in the YYYY-MM-DD format
    and prints it.
    """

    if not re.search(r'\d\d\d\d-\d\d-\d\d$', this_date):
        raise ValueError('please submit date in YYYY-MM-DD format')

    print ('the submitted date is {0}'.format(this_date))

process_date()
