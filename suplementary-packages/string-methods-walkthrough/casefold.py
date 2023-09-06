'''
Casefold
    - converts text to deal with case sensitivity.
'''

text = 'MaRio'
print(text.casefold())

text2= "MaRIO"
print(text2.casefold())

print(text == text2)
print(text.casefold() == text2.casefold())