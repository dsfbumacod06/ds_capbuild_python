'''
You are given a sequence of zeros and ones, with each operation, you are allowed to remove consecutive equal elements, if no more groups of consecutive elements remain, how many operations will it take to remove all of the elements from the given sequence. # noqa
arr = [0, 1, 1, 1, 0] yields 2
[0, 1, 1, 1, 0] -> [0, 0] -> []
arr = [0, 1, 0, 0, 0, 0] yields 3
[0, 1, 0, 0, 0, 0] -> [0, 1] -> [0] -> []
'''

#  MY CODE
#  not optimized, function must return the least amount of operations
# def array_erasing(lst):
#     index_set = set()
#     eval_item = 100
#     if len(lst) == 0:
#         return 0
#     for index, item in enumerate(lst[:-1]):
#         if item == lst[index+1]:
#             if eval_item != 100:
#                 if eval_item == item:
#                     index_set.update([index, index+1])
#             else:
#                 index_set.update([index, index+1])
#                 eval_item = item  # current value being evaluated, must break if different na # noqa
#         else:
#             if eval_item != 100:
#                 break
#     if index_set:
#         index_set = list(sorted(index_set))
#         del lst[index_set[0]:index_set[-1]+1]
#     else:
#         lst.pop(0)
#     return 1 + array_erasing(lst)


# Video Code
# def array_erasing(lst):
#     if len(lst) == 0:
#         return 0
#     if len(lst) == 1:
#         return 1
#     consecutive_streaks = []
#     idx = 0
#     while idx < len(lst) - 1:
#         if lst[idx] == lst[idx + 1]:
#             opposite = 0 if lst[idx] == 1 else 1
#             if opposite in lst[idx:]:
#                 opposite_index = idx + lst[idx:].index(opposite)
#                 consecutive_streaks.append((idx, opposite_index-1))
#                 idx = opposite_index
#             else:
#                 consecutive_streaks.append((idx, len(lst)-1))
#                 idx = len(lst) - 1
#         else:
#             idx += 1
#     if consecutive_streaks == []:
#         if len(lst) > 2:
#             return 1 + array_erasing(lst[0:0] + lst[2:])
#         else:
#             return 2
#     steps = []
#     for streak in consecutive_streaks:
#         steps.append(1 + array_erasing(lst[:streak[0]] + lst[streak[1]+1:]))
#     # print(steps)
#     return min(steps)


# solution code
from itertools import groupby


def array_erasing(lst):
    a = [len(tuple(g)) for _, g in groupby(lst)]
    n = 1
    return a


if __name__ == "__main__":
    arr = [0, 1, 1, 1, 0, 0]  # 2
    # print(array_erasing(arr))
    for key, group in groupby(arr):
        print(f'key: {key}, group: {tuple(group)}')
    # arr = [0, 1, 0, 0, 0, 0]  # 3
    # print(array_erasing(arr))
    # arr = [0, 0, 0, 1, 1, 1, 1, 0, 1, 1]  # 3
    # print(array_erasing(arr))
    # arr = [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
    # print(array_erasing(arr))
    # arr = [1, 0, 1, 0, 1, 0]
    # print(arr)
    # print(arr[0:0])
    # print(arr[2:])
    # print(arr[0:0] + arr[2:])
