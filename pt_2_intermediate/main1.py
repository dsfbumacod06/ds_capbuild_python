# classes and objects

class Person:
    amount = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1
    
    def __del__(self):
        print(f'{self.name} has been evicted')
        Person.amount -= 1

    def __str__(self):
        values = f'{"name" : self.name,"age" : self.age,"height" : self.height}'
        return values

    def getOlder(self,years):
        self.age += years

if __name__ == '__main__':
    person1 = Person("Danica", 16, 199)
    person2 = Person("Jennie", 17, 167)
    person3 = Person("Jisoo", 24, 154)
    person4 = Person("Jennifer", 19, 180)
    print(Person.amount)
    del person2
    del person1
    print(Person.amount)
    input()
