'''
maketrans

translate
'''

text = "Anna Banana Loves Some Banana"
table = text.maketrans("an", "🐒🍌")

print(text.translate(table))