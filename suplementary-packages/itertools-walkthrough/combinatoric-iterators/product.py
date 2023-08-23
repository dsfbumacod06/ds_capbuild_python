'''
Product
    - get the cartesian product of the list
    - products of 2 sets
    - repeat value duplicates the combination n times, resulting in a larger product set
'''
import itertools

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']

product = itertools.product(lst1, lst2, repeat=2)


for prod in list(product):
    print(prod)

# print(list(product))