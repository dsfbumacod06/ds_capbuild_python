'''
String Formatting with F-Strings
'''

name = "Mike"
age = 25
# print("Hello my name is %s and I am %d years old!"%(name,age))
# print("Hello my name is {} and I am {} years old!".format(name,age))
# print(f"Hello my name is {name} and I am {age} years old!") # we can pass code inside the braces

favoritenumber = 19.123456789101112

print("Hello my name is %s and I am %d years old! My favorite number is %.2f"%(name,age,favoritenumber))
print(f"Hello my name is {name} and I am {age} years old! My favorite number is {favoritenumber:.2f}")