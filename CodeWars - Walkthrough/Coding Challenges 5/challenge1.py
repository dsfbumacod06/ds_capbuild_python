'''
Digit Symmetry
1176 -> 1176 Squared (1176 * 1176) = 1382976
1176
    - first two digits of 1176 form a prime
1382976
    - first two digits of 1382976 form a prime
1176 and 1382976
    - last two digits are the same


Given two numbers representing a range (a, b).
How many numbers satisfy this property within that range? a <= n < b

Example:
solve(2, 1200) yields 1 since only 1176 solves this property
within the range 2 <= n < 1200
'''


# mycode
# def solve(a, b):
#     prime_nums = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]  # noqa
#     matches = 0
#     # matching = 0
#     if a < 11:
#         a = 11
#     for i in range(a, b):
#         if int(str(i)[:2]) in prime_nums:
#             if int(str(i**2)[:2]) in prime_nums:
#                 if int(str(i)[-2:]) == int(str(i**2)[-2:]):
#                     # matching = i
#                     matches += 1
#     return matches

# solutions
def solve(a, b):
    PN = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]  # noqa
    # return sum(1 for i in range(a, b) if int(f'{i}'[:2]) in PN and int(f'{i**2}'[:2]) in PN and i%100 == (i**2)%100)   # noqa
    return sum(1 for i in range(a, b) if int(str(i)[:2]) in PN and int(str(i**2)[:2]) in PN and (i**2 -i )%100 == 0)   # noqa


print(solve(2, 1200))
print(solve(2, 10000))
print(solve(2, 100000))
print(solve(2, 1000000))
print(solve(100000, 1000000))
