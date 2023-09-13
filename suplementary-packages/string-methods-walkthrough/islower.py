'''
isLower
    - checks if entire string is lowercase.
    - ignores non-letters
'''

text = "Abc"
print(text.islower())  # false
text = "abc"
print(text.islower())  # true
text = "abC"
print(text.islower())  # false
text = "1bc"
print(text.islower())  # true
text = "1b234567"
print(text.islower())  # true
text = "1123"
print(text.islower())  # false
text = "999Z"
print(text.islower())  # false

