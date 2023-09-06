'''
Swapping Variables
'''

# x, y, z = 1, 2, 3
# print(x, y, z)
# x, y, z = z, y, x
# print(x, y, z)

a = 10
b = 20


'''
Bit-wise Swapping


a = 1010
b = 10100

XOR - 1 if different, 0 if the same

24 = 011000 -> a
41 = 101001 -> b
XOR: 110001 -> MASK -> a
XOR: 011000 -> 41 XOR MASK = 24




24 = 011000 -> a
41 = 101001 -> b

a XOR b:
011000
101001
110001 -> MASK

MASK XOR b
110001
101001
011000 -> a

MASK XOR a
110001
011000
101001 -> b
'''

a = a ^ b  # MASK
b = b ^ a  # 10, value of a
a = a ^ b  # 20, value of b
print(a)
print(b)
