'''
Docstrings
'''


def myExpo(num1, num2):
    '''
    This function takes one number to the power of
    another number and returns the result

    :param num1: This is the base
    :param num2: This is the exponent
    :return: This is the result of the calculation
    '''
    return num1 ** num2


print(myExpo(5, 4))
print(help(myExpo))
print(myExpo.__doc__)
