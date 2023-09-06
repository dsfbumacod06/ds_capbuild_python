'''
Decorators
adds a certain functionality to a function
wraps a function with ano ther functionality
'''


def mydecorator(function):
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("I am decorating your function") #executes the decorator before executing the return block
        return return_value

    return wrapper


@mydecorator
def hello(person):
    print(f"Hello {person}!!!!!")
    return f"Hello {person}!"



print(hello("Mike"))