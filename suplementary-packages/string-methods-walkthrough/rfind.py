'''
rfind
    - find the first occurence of a character closes to the end of the string.
    - returns -1 if no match found.
'''

text = "A: Some text. A"
position = text.find("A")
print(position)
position = text.rfind("A")
print(position)