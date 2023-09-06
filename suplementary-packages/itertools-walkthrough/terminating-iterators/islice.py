'''
iSlice
works the same as list slicing
'''
import itertools

lst = ['a', 'b', 'c', 'd', 'e']

sliced = itertools.islice(lst, 2, None)
print(list(sliced))
sliced = itertools.islice(lst, 2)
print(list(sliced))
sliced = itertools.islice(lst, 2, 4)
print(list(sliced))
sliced = itertools.islice(lst, 0, 4, 2)
print(list(sliced))
