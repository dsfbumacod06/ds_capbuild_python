'''
Factory Design Pattern
    - Increase Modularity
'''
from abc import ABCMeta,abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    @abstractstaticmethod
    def person_method():
        """Interface Method"""


class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Name" 
    # person method needs to be overwritten

    def person_method(self):
        print("I am a Student")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name" 
    # person method needs to be overwritten

    def person_method(self):
        print("I am a Teacher")


# s1 = Student()
# s1.person_method()
# t1 = Teacher()
# t1.person_method()

''' 
Decide whether a person will be a teacher or student at runtime:

Using code:
choice = input("Type: ")
if choice == "Student" . . .  
'''

class PersonFactory:
    @staticmethod
    def buildPerson(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1 # can raise exception if needed
    

if __name__ == "__main__":
    choice = input("What type of person do you want to create? ")
    person = PersonFactory.buildPerson(choice)
    person.person_method()
