'''
Zip Function
    - combines iterables into tuples or collections of individual values
'''

names = ['Jenny', 'Jisoo', 'Rose', 'Lisa']
ages = [21, 22, 20, 19]
songs = ['Solo', 'Flower', 'On The Ground', 'Lalisa']

# for i in range(len(names)):
#     print(f"Name: {names[i]}, Age: {ages[i]}")

# print(list(zip(names, ages)))
for name, age, song in zip(names, ages, songs):
    print(f"Name: {name}, Age: {age}, Solo: {song}")
