import sys
# Trapping two exceptions at the same time
try:
    arg = sys.argv[1]
    num = int(arg)

except(IndexError, ValueError):
    exit("please enter an integer on the command line")

print("thanks for the int")
