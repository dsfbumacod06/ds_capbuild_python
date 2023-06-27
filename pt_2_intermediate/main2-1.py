# inheritance

import json
import ast

class Person:
    amount = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1
    
    def __del__(self):
        # print(f'{self.name} has been evicted')
        Person.amount -= 1

    def __str__(self):
        values = {"name" : self.name,"age" : self.age,"height" : self.height}
        return str(values)

    def getOlder(self,years):
        self.age += years


class Worker(Person):
    def __init__(self, name, age, height,salary):
        super(Worker,self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        text = super(Worker,self).__str__()
        json_text = ast.literal_eval(text)
        json_text["salary"] = self.salary
        return str(json_text)
    
    def calculate_yearly_salary(self):
        return self.salary * 12




person1 = Person("Danica", 16, 199)
person2 = Person("Jennie", 17, 167)
person3 = Person("Jisoo", 24, 154)
person4 = Person("Jennifer", 19, 180)
worker1 = Worker("Annie", 41, 139, 5000)
print(worker1)
print(worker1.calculate_yearly_salary())


