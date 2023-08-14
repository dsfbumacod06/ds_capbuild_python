from sample2 import addIt

# command = 'Hello, World!'
# match command:
#     case 'Hello, World!':
#         print('Hello to you too!')
#     case 'Goodbye, World!':
#         print('See you later')
#     case other:
#         print('No match found')

x = [4, -5, 6]
# y = lambda x: abs(x//2)
z = list(map(lambda x: abs(x//2), x))
print(z)

print(addIt(6, 8))
