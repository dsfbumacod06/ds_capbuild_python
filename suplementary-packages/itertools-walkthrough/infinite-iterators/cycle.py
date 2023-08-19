# Cycle
# take a list and create an infinite loop over it.

import itertools

l = ['A', 'B', 'C']  # noqa
cycler = itertools.cycle(l)

for i, letter in enumerate(cycler):
    print(f'index: {i}, letter: {letter}')
    if i == 20:
        break
