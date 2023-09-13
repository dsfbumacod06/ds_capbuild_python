'''
lstrip
    - removes text that matches the beginning of the string
    - removes all matching text as long as found at the start of the string.
'''

text = "Some text."
print(text.lstrip("Some "))
print(text.lstrip("text"))
text = "babababanana"
print(text.lstrip("ba"))