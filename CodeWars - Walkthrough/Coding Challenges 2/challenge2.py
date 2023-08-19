""""
Bit Counting
Write a function that takes an integer as input, and returns the
number of bits that are equal to the one in the binary representation
of that number. You can guarantee that the input is non-negative.

Example:
   1234 -> 10011010010
 - 6kyu Hardness
"""



# My Code
def count_bits(n):
    return bin(n).count("1")



#Refactor

# Video Implementation / Alternate Implementations



# My Test
if __name__ == '__main__':
    print(count_bits(1234))
