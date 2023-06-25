'''
Decorators
Timing
'''
import time

def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args,**kwargs)
        with open('main2-logfile.txt','a+') as f:
            fname = function.__name__
            # print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args,**kwargs)
        after = time.time()
        fname = function.__name__
        print(f'{fname} took {after - before} seconds to execute!')
        return value

    return wrapper


@logged
@timed
def myfunction(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result


x = myfunction(100000)