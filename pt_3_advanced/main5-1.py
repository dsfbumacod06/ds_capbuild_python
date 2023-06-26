'''
Encapsulation
'''

class Person:
    def __init__(self, name, age, gender):
        self.__name = name # adding "__" before an attribute sets it as a private property
        self.__age = age
        self.__gender = gender
    
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self,value): # can add value checks if necessary
        if value == "Jennypurr":
            self.__name = "Jisooya"
        else:
            self.__name = value

    @staticmethod
    def mymethod(): #not related to the class itself
        print("Hello World")

p1 = Person("Mike", 23, "M")
# print(p1.__name) # does not work
print(p1.Name)
p1.Name = "Jennypurr"
print(p1.Name)

Person.mymethod()
p1.mymethod()


def dosth(param: list[int]):
    pass