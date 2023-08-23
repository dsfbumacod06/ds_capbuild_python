'''
Starmap
passes the elements of the list as arguments to a function
arguments/elemnts are must be iterable
'''

import itertools
from operator import pow

lst = [(2, 3), (2, 4), (2, 5)]
starmapped = itertools.starmap(pow, lst)
print(list(starmapped))


lst2 = [2, 2, 2]
lst3 = [3, 4, 5]
mapped = map(pow, lst2, lst3)
print(list(mapped))