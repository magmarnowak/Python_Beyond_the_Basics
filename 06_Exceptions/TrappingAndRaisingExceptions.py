import sys

myDict = {'a':1, 'b':2, 'c':3, 'd':4}

key = input('please input a key: ')

try:
    print('testing for error')
    print('the value for {0} is {1}'.format(key, myDict[key]))

except KeyError:
    print('trapped error')
    print("they key {0} does not exsist".format(key))
    # sys.exit()

print('program continues...')    
