'''
isnumeric
    - true if text only contains a numeric value.
'''

text1 = "½⅕ⅣⅮⅳⅺ⒘⒏⑻"

print(text1.isdecimal())
print(text1.isdigit())
print(text1.isnumeric())