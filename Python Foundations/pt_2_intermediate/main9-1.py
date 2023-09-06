# recursion
'''
9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
9! = 9 * 8!
9! = 9 * 8 * 7!
. . .
'''

# non-recursive way
# n = 7 
# fact = 1
# while n > 0:
#     fact = fact * n
#     n -= 1

# print(fact)

# recursive way
def factorial(n):
    if n < 1:
        return 1
    else: 
        number = n * factorial(n-1)
        return number
    
print(factorial(7))