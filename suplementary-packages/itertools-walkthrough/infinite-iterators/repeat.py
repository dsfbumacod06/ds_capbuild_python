# Repeat

import itertools as iter

string = 'String'
repeater = iter.repeat(string, 10)  # gets consumed
# print(repeater)
for i, text in enumerate(repeater):
    print(f'{i},{text}')
    if i == 5:
        break

print(list(repeater))

# for text in repeater:
#     print(text)

# for text in iter.repeat('ASHLEY!! TIGNAN MO AKO', 10):
#     print(text)
