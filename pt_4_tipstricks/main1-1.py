'''
List Comprehensions
    - concise way of creating lists
'''

numbers = [18,16,22,99,23,11,54]

# create even numbers list

# normal way
# new_list = []
# for number in numbers:
#     if number%2 == 0:
#         new_list.append(number)
# print(new_list)

# list comprehension
new_list = [x for x in numbers if x%2==0]
print(new_list)

