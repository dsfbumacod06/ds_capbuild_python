'''
Power set

'''

# import itertools


# def power(a):
#     combs = []
#     for i in range(0, len(a)+1):
#         for item in list(itertools.combinations(a, i)):
#             combs.append(list(item))
#     return combs


def power(s):
    set1 = [[]]
    for num in s:
        set1 += [x+[num] for x in set1]
    return set1


print(power([1, 2, 3]))
