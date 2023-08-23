'''
Takewhile
opposite of dropwhile
'takes' the elements as long as the condition/function evaluates to true, and then ignores the rest of the list
'''

import itertools

lst = [1, 2, 3, 4, 5, 6, 1]

take = itertools.takewhile(lambda x: x < 4, lst)
print(list(take))