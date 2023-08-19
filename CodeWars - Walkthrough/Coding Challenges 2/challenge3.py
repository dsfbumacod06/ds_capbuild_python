""""
Compare Squares
Given two arrays, wrute a fybctuib comp(a,b), that checks whether the two arrays have the same elements with the 
same multiplicities. Same meanins here that the elements in b are the elements in a squared regardless of the order.

Example:
a = [121, 144, 19, 161, 19, 144, 19,11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
 - 6kyu Hardness
"""



# My Code
# def comp(array1, array2):
#     array1 = [pow(x,2) for x in array1]
#     return array1.sort() == array2.sort()



#Refactor

# Video Implementation / Alternate Implementations
def comp(array1, array2):
    if (array1 == None) or (array2 == None):
        return False
    temp_array = [x ** 2 for x in array1]
    return sorted(temp_array) == sorted(array2)


# My Test
if __name__ == '__main__':
    a = [121, 144, 19, 161, 19, 144, 19,11]
    b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    print(comp(None,None))
