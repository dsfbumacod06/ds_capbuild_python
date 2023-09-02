'''
Generators
'''

# Seq from 1 to 9,000
# cube each number
# [1, 2, . . . 90000] ** 3
# for x in range(1,9000000):
#     print(x ** 3)

# Generators - Lazy Execution
# [2..90] -> numbers 2 to 90
# produces what we need when we need it

def mygenerator(n):
    for x in range(n):
        yield x ** 3        

values = mygenerator(9000000)
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
# for x in values:
#     print(x)




