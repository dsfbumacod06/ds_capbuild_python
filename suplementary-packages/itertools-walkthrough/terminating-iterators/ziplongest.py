'''
zip longest
'''

import itertools

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = [True, False]

# zipped = zip(a, b, c)  # uses the shortest list
# zipped_longest = itertools.zip_longest(a, b, c)  # fillvalue = None by default
zipped_longest = itertools.zip_longest(a, b, c, fillvalue='Jennyfer')

for a, b, c in zipped_longest:
    print(a, b, c, sep=' : ')