'''
Decorators
adds a certain functionality to a function
wraps a function with ano ther functionality
'''


def mydecorator(function):
    def wrapper():
        function()
        print("I am decorating your function")
        
    return wrapper


def hello_world():
    print("Hello World!")

mydecorator(hello_world)() # calls the function, and calls the result

