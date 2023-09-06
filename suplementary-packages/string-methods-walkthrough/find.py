'''
Find
    - returns the first/lowest occurence of a substring.
    - -1 if not in the string
'''


text = "Anna Banana Anana Bannana"
position = text.find("Anana")
print(position)
print(text[position])
print(text[position:position+5])