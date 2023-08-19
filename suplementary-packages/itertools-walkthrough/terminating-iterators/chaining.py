'''
Chaining
combines iterables

'''


import itertools as iter

a = [1, 2, 3]
b = ['a', 'b', 'c']

combined = iter.chain(a, b, b, a)

print(list(combined))


lst = ['a', 'b', 'c', 'd']
