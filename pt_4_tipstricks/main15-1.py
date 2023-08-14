'''
Most Frequent Value 
'''

# from collections import Counter

myList = [1, 2, 3, 4, 5, 4, 3, 5, 5, 6, 7, 7, 9, 2, 2, 2]

# counter = Counter(myList)
# print(counter.most_common(1))  # returns tuples, value, occurence
# print(f"Value: {counter.most_common(1)[0][0]}, Occurence: {counter.most_common(1)[0][1]}")  # noqa
# mySet = set(myList)
print(max_val := max(set(myList), key=myList.count))
print(myList.count(max_val))
