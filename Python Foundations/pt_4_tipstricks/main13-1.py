'''
Merging Dictionaries
'''

dict1 = {'a': 1, 'b': 7}
dict2 = {'b': 4, 'c': 8}

# print(dict1 + dict2)  # does not work

# USING UPDATE
# using update either changes dict1 and dict2, merge is not stored elsewhere
# dict1.update(dict2) # updates the values of dict 1 with the values of dict2
# dict2.update(dict1)  # updates the values of dict 2 with the values of dict1
# print(dict2)


# USING **kwargs operator
# dict3 = {**dict1, **dict2}
# dict3 = {**dict2, **dict1}
# print(dict3)

# USING the pipelin (|) operator (python 3.9 onwards)
dict3 = dict1 | dict2
# dict4 = dict1 |= dict2 # (does not work?)
# dict3 = dict(dict1.items() | dict2.items())  # inconsistent value of b
print(dict3)
