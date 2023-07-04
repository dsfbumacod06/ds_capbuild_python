'''
Lambda Expressions
'''

# mysquare = lambda x: x*x
# mysum = lambda x,y: x+y
# mysum = lambda *args: sum(args)
# print(mysum(5,14,12,31,234))
# print((lambda x: x ** 3)(5))

# practical examples
# can be used to pass functions into functions
# for functions only used once
numbers = [ 8, 66, 12, 14, 15, 7, 99, 109, 88, 76]

even_nums = list(filter(lambda x: x%2==0,numbers))
print(even_nums)

squared_numes = list(map(lambda x: x **2, numbers))
print(squared_numes)


# returns a function that you can customize
def multiplier(num):
    return lambda x: x*num

ten_multiplier = multiplier(10)

print(ten_multiplier(5))