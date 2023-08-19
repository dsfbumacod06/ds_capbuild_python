'''
FilterFalse

Everything evaluated as false will be returned
'''


import itertools

lst = range(100)

filtered = itertools.filterfalse(lambda n: n % 10, lst)  # will return 0 to numbers divisible by 10, hence falsy value # noqa
print(list(filtered))
