'''
arr = [0, 1, 1, 1, 0] yields 2
[0, 1, 1, 1, 0] -> [0, 0] -> []
arr = [0, 1, 0, 0, 0, 0] yields 3
[0, 1, 0, 0, 0, 0] -> [0, 1] -> [0] -> []
'''

# def array_erasing(lst):
#     steps = 0
#     index_set = {}
#     counter = 0
#     for index, item in enumerate(lst):
#         if item == lst[index + 1]:
#             index_set.update(index, index+1)
#     if index_set:
#         for index in index_set:
#             lst.pop(index)
#         step += 1
#     else
#     return lst


def array_erasing(lst):
    index_set = set()
    if len(lst) == 0:
        return 1
    for index, item in enumerate(lst[:-1]):
        if item == lst[index+1]:
            index_set.update([index,index+1])
    if index_set:
        index_set = list(sorted(index_set))
        del lst[index_set[0]:index_set[-1:]]
    else:
        lst.pop(0)
    return 1 + array_erasing(lst)

# def get_arr_len(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         arr.pop()
#         return 1 + get_arr_len(arr)



if __name__ == "__main__":
    arr = [0, 1, 1, 1, 0]
    # print(array_erasing(arr))
    print(array_erasing(arr))
    # my_set = set()
    # my_set.update([3,2,1])
    # sorted(my_set)
    # # print(list(my_set)[-1:])
    # del arr[1:3]
    # print(arr)