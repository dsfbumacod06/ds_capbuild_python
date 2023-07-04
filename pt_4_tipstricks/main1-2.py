'''
List Comprehensions
    - concise way of creating lists
'''

numbers = [1,2,3,4,5,6,7]

# powers_of_two = [2**x for x in numbers]
powers_of_two = [2**x for x in range(30) if x%5 == 0]
print(powers_of_two)



