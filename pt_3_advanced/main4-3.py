'''
Argument Parsing Kineso
'''

import sys
import getopt

#usage: main.py FILENAME -[c] argument
filename = 'main4.txt'
message = 'default'

opts, args = getopt.getopt(sys.argv[1:],"f:m:", ['filename','message'])

print(opts)
print(args)

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)