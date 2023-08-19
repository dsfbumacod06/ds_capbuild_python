""""
Your goal in this kata is to implement a differene function,
which subtracts one list from another, and returns the result.
It should remove all values from list a, which are present in b,
keeping their order.
Example:
    array_diff([1,2],[1]) -> [2]
    array_diff([1,2,2,2,2,3],[2]) -> [1,3]
 - 6kyu Hardness
"""



# My Code
def array_diff(a,b):
    return [element for element in a if element not in b]


#Refactor

# Video Implementation / Alternate Implementations




# My Test
if __name__ == '__main__':
    print(array_diff([1,2],[1])) # -> [2]
    print(array_diff([1,2,2,2,2,3],[2])) # -> [1,3])
