'''
Dropwhile

DROPS the values of the list WHILE the condition is true.
then returns everything that comes after it, regarless of the condition
'''
import itertools


# def lessThree(num):
#     return num < 3


nums = [1, 2, 3, 4, 5, 6, 7, 1, 1, 1]
remaining = itertools.dropwhile(lambda n: n < 3, nums)
# remaining = itertools.dropwhile(lessThree, nums)
print(list(remaining))
