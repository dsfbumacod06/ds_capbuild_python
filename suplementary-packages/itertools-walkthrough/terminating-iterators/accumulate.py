# Accumulate passes the values of the list as arguments
# incrementing per index (accumulates)
# applies the sum function by default

import itertools as iter
import operator


def sample_func(*args):
    str_lst = []
    for arg in args:
        str_lst.append(arg)
    return ':'.join(str_lst)


nums = [1, 2, 3, 4, 5]
accumulation = iter.accumulate(nums, operator.mul)
words = ['one', 'two', 'three']
w_acc = iter.accumulate(words, sample_func)

print(list(w_acc))
