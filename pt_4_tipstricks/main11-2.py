'''
Zip Function
'''

sales = [100, 150, 295, 1000]
costs = [150, 150, 200, 500]

# for sale, cost in zip(sales, costs):
#     print(f'Profit: {sale-cost}')

'''
Unzipping
'''

zipped = [('Jenny', 21), ('Jisoo', 23), ('Rose', 20), ('Lisa', 19)]
names, ages = zip(*zipped)  # returns tuples
# print(list(names))
# print(list(ages))

'''
Another Example
'''

letters = ['b', 'd', 'a', 'c']
numbers = [3, 2, 4, 1]

data1 = sorted(zip(letters, numbers))  # connected data, sorted by one of which
data2 = sorted(zip(numbers, letters))  # same as above, different sorting data
# print(data1)
# print(data2)

'''
Lists to Dictionaries
'''
# myDict = dict(zip(letters, numbers))
myDict = {key: value for key, value in zip(letters, numbers)}
print(myDict)


# unpacking from yt shorts
# first, *_, secondLast, last = letters
# print(first, secondLast, last)
