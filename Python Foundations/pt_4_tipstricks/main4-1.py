'''
Ternary Operator
'''


age = 18

# normal way
# if age >= 18:
#     adult = True
# else:
#     adult = False

# if adult:
#     print("You are an adult")
# else:
#     print("You are not an adult")


# Ternary Operator
# print("You are an adult") if age >=18 else print("You are not an adult")
# print("You are an adult" if age>=18 else "You are not an adult")

adult = True if age>=18 else False
print("You are an adult" if adult else "You are not an adult")



