# Raising exceptions:

def make_delim_line(list_to_join, delim):

    try:
        formatted_line = delim.join(list_to_join)
    except TypeError:
        raise TypeError("make_delim_line(): arg 1 must be a list or tuple")
    return formatted_line

fline = make_delim_line(100,',')

myDict = {'a':1, 'b':2, 'c':3, 'd':4}

# try:
#     print(5/0)
# except ZeroDivisionError, e:
#     print(e.message)
#     print(e.args)
