""""
Your task is to make a function that can take any non-negative integer as an argument and
return with its digits in descending order. Essentially rearrage the digits to create 
the highest possible number.

Example:
    42145 -> 54421
    145263 -> 654321
    123456789 -> 987654321
 - 7kyu Hardness
"""



# My Code
# def descending_number(num):
#     digits = [number for number in str(num)]
#     digits.sort(reverse=True)
#     return int("".join(digits))



#Refactor

# Video Implementation / Alternate Implementations
def descending_number(num):
    # return int("".join(sorted([x for x in str(num)], reverse=True)))
    return int("".join(sorted(str(num), reverse=True)))

    # string cannot be sorted usting string sort but can be using python sorted


# My Test
if __name__ == '__main__':
    print(descending_number(42145))
    print(descending_number(145263))
    print(descending_number(123456789))
