'''
tee
creates an independent list of copies
'''
import itertools

lst = [1, 2, 3, 'a', 'b', 'c']

tee = itertools.tee(lst, 3)

for t in tee:
    print(list(t))

tee = itertools.tee(lst, 4)
print([list(t) for t in tee])