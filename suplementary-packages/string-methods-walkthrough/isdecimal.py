'''
isdecimal
    - true if text only numbers
    - if a string is decimal, it is also a digit, and numeric
'''

text1 = "123"

print(text1.isdecimal())
print(text1.isdigit())
print(text1.isnumeric())