'''
isPrintable
    - returns false if text does not contain escape characters such as new line, etc.
'''

text = "some text \n"
print(text.isprintable())  # False
text = "some text \t"
print(text.isprintable())  # False
text = "some text \\t"
print(text.isprintable())  # True
text = "some text"
print(text.isprintable())  # False