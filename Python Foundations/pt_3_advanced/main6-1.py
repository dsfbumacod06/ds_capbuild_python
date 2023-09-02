'''
Type Hinting
'''

def myfunction(myparameter: int) -> int:
    # return f"{myparameter + 10}"
    return myparameter + 10

def otherfunction(otherparameter: str):
    print(otherparameter)
#mypy - type hinting tool/library
# mypy main6-1.py


# print(myfunction(10))
otherfunction(myfunction(20))