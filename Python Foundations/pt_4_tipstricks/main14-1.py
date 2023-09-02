'''
Slice Function
'''

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[:-2])

#  parameters -> start element, stop element, step size
LASTFOUR = slice(-4, None)
FIRSTFOUR = slice(4)
EVERYOTHER = slice(0, None, 2)
print(f'First four: {numbers[FIRSTFOUR]}')
print(f'Last four: {numbers[LASTFOUR]}')
print(f'Every other: {numbers[EVERYOTHER]}')

mytext = "Anna Banana I love you a bunch."
print(f'Text: {mytext[EVERYOTHER]}')
