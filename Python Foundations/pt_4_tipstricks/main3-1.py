'''
The Map Function
    - maps a function to an iterable object
'''

numbers = [ 14, 23, 8, 12, 2, 5, 90]

def square(x):
    return x*x

# normal way
# new_list = []
# for i in numbers:
#     new_list.append(square(i))


# list comprehension
# new_list = [square(i) for i in numbers]
# new_list = [x*x for x in numbers]


# map function -> same efficiency as list comprehension
new_list = list(map(square,numbers))


print(new_list)