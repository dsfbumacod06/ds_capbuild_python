# Python code to demonstrate working of
# Deleting all occurrences of character
# Using translate()

# initializing string
test_str = "GeeksforGeeks"
res = test_str.translate(str.maketrans({'e':None}))

# printing result
# print(str(res))
print(test_str)
print(res)

print(len(test_str))
print(len(test_str.translate(str.maketrans({'e':None}))))
