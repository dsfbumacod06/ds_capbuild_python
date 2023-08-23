'''
Pairwise
- returns an overlapping pairs of a list
'''
import itertools

lst = 'abcde'
paired = itertools.pairwise(lst)
print(list(paired))
