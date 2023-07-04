'''
Composite Design Patern
    - multiple classes that inherit from a parent class.
    - each class can also consist of other classes.
    - Continents -> Countries -> Regions
    - Hierarchal -> Tree-like
'''

from abc import ABCMeta,abstractmethod, abstractstaticmethod

class IDepartment(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self,employees):
        """implement in child class"""

    @abstractstaticmethod
    def print_department():
        """implement in child class"""


class Accounting(IDepartment):
    def __init__(self,employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Department: {self.employees}")

class Development(IDepartment):
    def __init__(self,employees):
        self.employees = employees

    def print_department(self):
        print(f"Development Department: {self.employees}")

class ParentDepartment(IDepartment):
    def __init__(self,employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self,dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print(f"Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees: {self.employees}")


dept1 = Accounting(200)
dept2 = Development(170)
pdept = ParentDepartment(30)
pdept.add(dept1)
pdept.add(dept2)

pdept.print_department()