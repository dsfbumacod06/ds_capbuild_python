'''
Reversing Lists
'''

names = ['Jenny', 'Jisoo', 'Rose', 'Lisa']


revList = []
for index in range(len(names)):
    revList.append(names[len(names) - index - 1])

# print(revList)  # least efficient
# print(list(reversed(names))) # does not change the list
# names.reverse()  # applies the reverse to the list
# print(names)
# print(names[::-1])
