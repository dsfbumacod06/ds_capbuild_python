'''
Argument Parsing Kineso
'''

import sys

#sys.argv 0 - filename 1 2 . . . n - positional arguments

# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv)

# Usage main.py FILENAME

filename = sys.argv[1]
message = sys.argv[2]
with open(filename, 'w+') as f:
    f.write(message)
 