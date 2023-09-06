'''
isdigit
    - true if text only contains a digit.
    - if a string is a digit, it is also numeric
'''

text1 = "⁷⑨⑧⑤"

print(text1.isdecimal())
print(text1.isdigit())
print(text1.isnumeric())