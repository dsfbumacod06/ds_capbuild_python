'''
Partition
    - split the string at a certain point
'''

text = "a + b = c"
print(text.partition("="))  # ("a + b ", "=", " c")
text = "a + b = c = a + b"
print(text.partition("="))  # ('a + b ', '=', ' c = a + b') 