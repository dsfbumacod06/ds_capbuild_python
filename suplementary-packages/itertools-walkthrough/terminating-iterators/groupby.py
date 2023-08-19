'''
GroupBy
'''
import itertools

lst = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('b', 5), ('c', 6)]

grouped = itertools.groupby(lst, lambda x: x[0])

# for key, values in grouped:
#     print(f'Key: {key}, Values: {list(values)}')


nums = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 2, 2]
num_groups = [list(g) for k, g in itertools.groupby(nums)]
print(num_groups)

# for key, values in itertools.groupby(nums):
#     print(f'Key: {key}, Values: {list(values)}')
