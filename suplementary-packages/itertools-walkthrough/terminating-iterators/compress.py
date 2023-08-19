'''
Compress
pairs a list with a 'selector' list.
indexes matched with the selector's truthy values are returned.
'''
import itertools

lst = ['a', 'b', 'c', 'd', 'e']
selectors = [0, 1, 1, 0, 1]
# selectors = [0, 1, 5, 0, 'anna']
compressed = itertools.compress(lst, selectors)
print(list(compressed))
