'''
Singleton Design Pattern
    - Normally in a class Person for example, we can have as much person 
    as the memory allows, but in this approach we can only have one.
'''


from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):

    @abstractstaticmethod
    def print_data():
        '''implement in child class'''


class PersonSingleton:
    
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None: # not created
            PersonSingleton("Default Name", 0) # create if not existing
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")

p = PersonSingleton("Mike",30)
p.print_data()


# p1 = PersonSingleton("Jennifer", 42)
p2 = PersonSingleton.get_instance()
print(p2.name)