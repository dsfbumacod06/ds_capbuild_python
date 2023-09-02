'''
Any and All
Any - true if at least 1 element is true
All - true if all values are true
'''
x = [True, False, True]
print(any(x))  # returns true
print(all(x))  # returns false

numbers = [12, 10, 88, 94]


# check if one or all is even
# even = lambda x: x % 2 == 0
def even(x): return x % 2 == 0


result = [even(number) for number in numbers]
if any(result):
    print('At least one number is even')
else:
    print('No number is even')
if all(result):
    print('All numbers are even')
