'''
Amount of Digits in a number
'''
# import math

number = 1_000_000_5
# number = 999_999_999_999_999_8  # returns 17 instead of 16, python represents numbers like this rounded up # noqa


# if number > 0:
#     print(int(math.log10(number))+1)
# elif number < 0:
#     print(int(math.log10(-number))+1)
# else:
#     print(1)

counter = 1
while number >= 10**counter:
    counter += 1
print(counter)