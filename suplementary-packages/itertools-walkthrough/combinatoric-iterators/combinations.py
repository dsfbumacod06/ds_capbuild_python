'''
Combinations
    - gets all the unique combinations of a list

Combinations with Replacement
    - allows elements to be repeated, eg: (1, 1, 1, 1)
'''
import itertools


# l = [0, 1, 2, 3, 4]
l = 'bcf'
l2 = 'bcbcf'

combinations = itertools.combinations(l, 2)
# combinations = itertools.combinations_with_replacement(l, 2)
for c in list(combinations):
    print(*c, sep=' : ')