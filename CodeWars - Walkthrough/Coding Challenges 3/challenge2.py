""""
Write a function that accepts an array of 10 integers (between 0 and 9)
that returns a string of those numbers in the form of a phone number
Example:
    create_phone_number([1,2,3,4,5,6,7,8,9]) # -> "(123) 456-7890"
 - 6kyu Hardness
"""



# My Code
def create_phone_number(n):
    # numbers = "".join([str(x) for x in n])
    # numbers = "".join(map(str,n))
    # return f"({numbers[:3]}) {numbers[3:6]}-{numbers[6:9]}"
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


#Refactor

# Video Implementation / Alternate Implementations




# My Test
if __name__ == '__main__':
    print(create_phone_number([1,2,3,4,5,6,7,8,9,0])) # -> "(123) 456-7890"
