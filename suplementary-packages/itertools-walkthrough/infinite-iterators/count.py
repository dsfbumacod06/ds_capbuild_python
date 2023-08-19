# COUNT
# generates evenly spaced numbers starting from [first argument]
# with step size [second argument]


import itertools
counter = itertools.count(10, 25)
for i in counter:
    print(i)
    if i >= 200:
        break
