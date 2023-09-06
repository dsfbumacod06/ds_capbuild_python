'''
LCS
Write a function called LCS that accepts two sequences and returns the
longest subsequence common to the passed in sequences.

Subsequence != Substring

Subsequence of abc => a b c ab ac bc abc


lcs("abcdef", "abc")  # abc
lcs("abcdef", "acf")  # acf
lcs("132535365", "123456789") # 12356
lcs("abc", "def") # ""
'''


import itertools


# my code
def my_lcs(lst1, lst2):
    filtered = list(itertools.filterfalse(lambda n: n not in lst1, lst2))
    shorter = [x for x in lst1 if x in filtered]
    longer = [x for x in lst2 if x in filtered]
    if len(shorter) > len(longer):
        shorter, longer = longer, shorter
    i = len(shorter)
    while i > 0:
        combs = itertools.combinations(shorter, i)
        for item in list(combs):
            if item in list(itertools.combinations(longer, i)):
                return "".join(item)
        i -= 1
    # return "None"


# video code
def subsequences(s):
    return set("".join(c) for i in range(len(s) +1) for c in itertools.combinations(s, i))  # noqa


def lcs(x, y):
    # return max(subsequences(x).intersection(subsequences(y)), key=len)
    return subsequences(x).intersection(subsequences(y))


print(my_lcs("zxyabcdef", "abczxy"))  # abc or zyx? video code returns abc, my code returns zxy  # noqa
# print(lcs("abcdef", "abc"))  # abc
# print(lcs("abcdef", "acf"))  # acf
# print(lcs("1325353651", "123456789"))  # 12356
# print(lcs("abc", "def"))  # ""
# print(lcs("anothertest", "notatest"))  # "notatest"
# print(lcs("finaltest", "zzzfinallyzz"))  # "final"

# print(subsequences("ann"))

'''
import itertools

lst = range(100)

filtered = itertools.filterfalse(lambda n: n % 10, lst)  # will return 0 to numbers divisible by 10, hence falsy value # noqa
print(list(filtered))
'''


# lst1 = "abcdbecfg"
# lst2 = "bcf"
# # print([x in lst1 for x in lst2])

# filtered = list(itertools.filterfalse(lambda n: n not in lst1, lst2))
# # print(filtered)
# lst1 = [x for x in lst1 if x in filtered]
# lst2 = [x for x in lst2 if x in filtered]
# shorter = lst1 if len(lst1) < len(lst2) else lst2  # bcf
# longer = lst2 if len(lst1) < len(lst2) else lst1  # bcbcf
# # print(shorter)
# # print(longer)

# i = len(shorter)
# while i > 0:
#     combs = itertools.combinations(shorter, i)
#     for item in list(combs):
#         if item in list(itertools.combinations(longer, i)):
#             print(item)
#     i -= 1
