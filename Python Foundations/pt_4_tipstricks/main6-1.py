'''
Enumeration
    - helpful in indexing data that is not indexed yet.
'''

myNames = ['Teddy', 'Bobby', 'Alex', 'Gabby', 'CJ', 'Mama', 'Princess']

'''
we want to, 0:Teddy, 1:Bobby . . . 6:Princess
'''

# usual way
# counter = 0
# for name in myNames:
#     print(f'{counter}: {name}')
#     counter +=1

print(list(enumerate(myNames)))
print(dict(enumerate(myNames)))
for index, name in enumerate(myNames):
    print(f'{index}:{name}')


