'''
List Comprehensions
    - concise way of creating lists
'''

words = [ "automobile", "car", "anger", "fox", "anchor"]
# new_words = [ word.upper() for word in words if word.startswith("a") else word]
new_words = [ word.upper() if word.startswith("a") else word for word in words]

print(new_words)

