'''
iterative vs recursive

implementing fibonacci sequence
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
'''

def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

print(fibonacci(3000))

def fibonacci2(n):
    if n <= 1:
        return n # can only be either 1 or 0
    else:
        return(fibonacci2(n-1) + fibonacci2(n-2))
    
print(fibonacci2(996))