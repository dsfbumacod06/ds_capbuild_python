'''
Ternary Operator
'''
# number = -1
# number = 1
# number = 11
# number = 101
number = 1001
print("This number is very very large" if number > 1000 else "This number is quite large" if number > 100 else "This number is small but still positive" if number > 0 else "The number is not positive")

