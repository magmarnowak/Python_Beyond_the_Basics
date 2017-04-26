"""
    Usages:
    ./assignment_3.py                           (reads out the entire config dict)
    ./assignment_3.py thiskey thisvalue         (sets 'thiskey' and 'thisvalue' in the dict)
"""


import sys
from assignment3 import ConfigDict

cd = ConfigDict('config_file.txt')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print("writing data: {0}, {1}".format(key, value))

    cd[key] = value

else:
    print("reading data")
    for key in cd.keys():
        print('    {0} = {1}'.format(key, cd[key]))

print(cd)
